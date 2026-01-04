<script>
  import { onMount } from 'svelte';
  
  let dailySpending = [
    { day: 'Mon', amount: 45 },
    { day: 'Tue', amount: 32 },
    { day: 'Wed', amount: 78 },
    { day: 'Thu', amount: 25 },
    { day: 'Fri', amount: 95 },
    { day: 'Sat', amount: 120 },
    { day: 'Sun', amount: 60 }
  ];
  
  let monthlyIncome = 0;
  let monthlyBudget = 0;
  let monthlySpending = 0;
  let userProfile = null;
  let newExpense = { description: '', amount: '', category: 'food' };
  let recentExpenses = [];
  
  // Additional chart data
  let categorySpending = [
    { category: 'Food', amount: 0, percentage: 0, color: 'from-green-400 to-emerald-500' },
    { category: 'Transport', amount: 0, percentage: 0, color: 'from-blue-400 to-cyan-500' },
    { category: 'Shopping', amount: 0, percentage: 0, color: 'from-purple-400 to-pink-500' },
    { category: 'Entertainment', amount: 0, percentage: 0, color: 'from-yellow-400 to-orange-500' },
    { category: 'Bills', amount: 0, percentage: 0, color: 'from-red-400 to-rose-500' }
  ];
  
  let weeklyTrend = [
    { week: 'Week 1', spending: 0 },
    { week: 'Week 2', spending: 0 },
    { week: 'Week 3', spending: 0 },
    { week: 'Week 4', spending: 0 }
  ];

  // Budget alert state
  let showBudgetAlert = false;
  let budgetAlertDismissed = false;
  
  // Check if over budget
  $: isOverBudget = monthlyBudget > 0 && monthlySpending > monthlyBudget;
  $: budgetPercentage = monthlyBudget > 0 ? (monthlySpending / monthlyBudget) * 100 : 0;
  $: isNearBudget = budgetPercentage >= 80 && budgetPercentage < 100;
  
  // Show alert when over budget
  $: if (isOverBudget && !budgetAlertDismissed) {
    showBudgetAlert = true;
  }
  
  function dismissBudgetAlert() {
    showBudgetAlert = false;
    budgetAlertDismissed = true;
  }

  // Load user profile from localStorage
  function loadUserProfile() {
    const storedProfile = localStorage.getItem('userProfile');
    if (storedProfile) {
      userProfile = JSON.parse(storedProfile);
      monthlyIncome = userProfile.monthlyIncome || 0;
      monthlyBudget = userProfile.monthlyBudget || 0;
    }
  }

  // Load data from backend
  async function loadDashboardData() {
    // First load from localStorage for immediate display
    loadUserProfile();
    
    try {
      // Load dashboard stats from backend
      const statsResponse = await fetch('http://localhost:5000/api/dashboard-stats', {
        credentials: 'include'
      });
      
      if (statsResponse.ok) {
        const stats = await statsResponse.json();
        // Backend values override localStorage if available
        if (stats.monthly_budget) monthlyBudget = stats.monthly_budget;
        if (stats.monthly_income) monthlyIncome = stats.monthly_income;
        monthlySpending = stats.monthly_spending || 0;
        
        // Update daily spending if available
        if (stats.daily_spending && stats.daily_spending.length > 0) {
          dailySpending = stats.daily_spending;
        }
      }

      // Load recent expenses
      const expensesResponse = await fetch('http://localhost:5000/api/expenses', {
        credentials: 'include'
      });
      
      if (expensesResponse.ok) {
        const data = await expensesResponse.json();
        recentExpenses = data.expenses.map(expense => ({
          description: expense.description,
          amount: expense.amount,
          category: expense.category,
          date: new Date(expense.date_added).toLocaleDateString()
        }));
        
        // Update category spending based on actual expenses
        updateCategorySpending();
      }
    } catch (error) {
      console.error('Error loading dashboard data:', error);
    }
  }
  
  function updateCategorySpending() {
    // Reset category amounts
    categorySpending.forEach(cat => {
      cat.amount = 0;
      cat.percentage = 0;
    });
    
    // Calculate from recent expenses
    recentExpenses.forEach(expense => {
      const category = categorySpending.find(c => c.category.toLowerCase() === expense.category.toLowerCase());
      if (category) {
        category.amount += expense.amount;
      }
    });
    
    // Calculate percentages
    const total = categorySpending.reduce((sum, cat) => sum + cat.amount, 0);
    if (total > 0) {
      categorySpending.forEach(cat => {
        cat.percentage = parseFloat(((cat.amount / total) * 100).toFixed(1));
      });
    }
    
    // Trigger reactivity
    categorySpending = [...categorySpending];
  }

  onMount(() => {
    loadDashboardData();
  });
  
  async function addExpense() {
    if (newExpense.description && newExpense.amount) {
      const expenseAmount = parseFloat(newExpense.amount);
      const newTotal = monthlySpending + expenseAmount;
      
      // Check if this expense will exceed budget
      const willExceedBudget = monthlyBudget > 0 && newTotal > monthlyBudget && monthlySpending <= monthlyBudget;
      const alreadyOverBudget = monthlyBudget > 0 && monthlySpending > monthlyBudget;
      
      try {
        // Submit to backend API
        const response = await fetch('http://localhost:5000/api/expenses', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
          body: JSON.stringify({
            description: newExpense.description,
            amount: expenseAmount,
            category: newExpense.category
          })
        });

        if (response.ok) {
          // Add expense to recent expenses list
          const expense = {
            description: newExpense.description,
            amount: expenseAmount,
            category: newExpense.category,
            date: new Date().toLocaleDateString()
          };
          
          recentExpenses = [expense, ...recentExpenses];
          
          // Update daily spending (add to today)
          const today = dailySpending[dailySpending.length - 1];
          today.amount += expenseAmount;
          dailySpending = [...dailySpending];
          
          // Update monthly spending
          monthlySpending += expenseAmount;
          
          // Update category spending
          updateCategorySpending();
          
          // Reset form
          newExpense = { description: '', amount: '', category: 'food' };
          
          // Show appropriate alert
          if (willExceedBudget) {
            budgetAlertDismissed = false;
            showBudgetAlert = true;
            alert('⚠️ Warning: This expense has exceeded your monthly budget!\n\nBudget: ₹' + monthlyBudget.toLocaleString() + '\nTotal Spent: ₹' + monthlySpending.toLocaleString() + '\nOver by: ₹' + (monthlySpending - monthlyBudget).toLocaleString());
          } else if (alreadyOverBudget) {
            alert('Expense added. Note: You are still over budget by ₹' + (monthlySpending - monthlyBudget).toLocaleString());
          } else {
            alert('Expense added successfully!');
          }
        } else {
          const error = await response.json();
          alert('Error adding expense: ' + error.error);
        }
      } catch (error) {
        console.error('Error:', error);
        // Still add locally even if backend fails
        const expense = {
          description: newExpense.description,
          amount: expenseAmount,
          category: newExpense.category,
          date: new Date().toLocaleDateString()
        };
        
        recentExpenses = [expense, ...recentExpenses];
        monthlySpending += expenseAmount;
        updateCategorySpending();
        newExpense = { description: '', amount: '', category: 'food' };
        
        // Show budget alert if exceeded
        if (willExceedBudget) {
          budgetAlertDismissed = false;
          showBudgetAlert = true;
          alert('⚠️ Warning: This expense has exceeded your monthly budget!\n\nBudget: ₹' + monthlyBudget.toLocaleString() + '\nTotal Spent: ₹' + monthlySpending.toLocaleString());
        } else {
          alert('Expense added locally (backend unavailable)');
        }
      }
    } else {
      alert('Please fill in all fields');
    }
  }
</script>

<div class="space-y-6">
  <h2 class="text-2xl font-bold text-white">Financial Assistant</h2>
  
  <!-- Budget Alert Banner -->
  {#if showBudgetAlert}
    <div class="bg-red-500/20 backdrop-blur-md p-4 rounded-xl border border-red-500/50 flex items-center justify-between animate-pulse">
      <div class="flex items-center">
        <span class="text-3xl mr-4">⚠️</span>
        <div>
          <h3 class="text-lg font-bold text-red-400">Budget Exceeded!</h3>
          <p class="text-white/80">You've spent ₹{(monthlySpending - monthlyBudget).toLocaleString()} more than your monthly budget of ₹{monthlyBudget.toLocaleString()}</p>
        </div>
      </div>
      <button 
        on:click={dismissBudgetAlert}
        class="text-white/70 hover:text-white transition-colors p-2"
      >
        ✕
      </button>
    </div>
  {/if}
  
  <!-- Near Budget Warning -->
  {#if isNearBudget && !isOverBudget}
    <div class="bg-yellow-500/20 backdrop-blur-md p-4 rounded-xl border border-yellow-500/50 flex items-center">
      <span class="text-3xl mr-4">⚡</span>
      <div>
        <h3 class="text-lg font-bold text-yellow-400">Approaching Budget Limit!</h3>
        <p class="text-white/80">You've used {budgetPercentage.toFixed(0)}% of your monthly budget. Only ₹{(monthlyBudget - monthlySpending).toLocaleString()} remaining.</p>
      </div>
    </div>
  {/if}
  
  <!-- Budget Overview -->
  <div class="grid md:grid-cols-4 gap-6">
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Monthly Income</h3>
      <p class="text-3xl font-bold text-emerald-400">₹{monthlyIncome.toLocaleString()}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Monthly Budget</h3>
      <p class="text-3xl font-bold text-green-400">₹{monthlyBudget.toLocaleString()}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Spent This Month</h3>
      <p class="text-3xl font-bold text-blue-400">₹{monthlySpending.toLocaleString()}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Remaining</h3>
      <p class="text-3xl font-bold {monthlyBudget - monthlySpending >= 0 ? 'text-purple-400' : 'text-red-400'}">₹{(monthlyBudget - monthlySpending).toLocaleString()}</p>
    </div>
  </div>
  
  <!-- Budget vs Spending Chart -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Budget vs Spending</h3>
    <div class="space-y-4">
      <div>
        <div class="flex justify-between text-white/70 mb-2">
          <span>Budget</span>
          <span>₹{monthlyBudget}</span>
        </div>
        <div class="w-full bg-white/20 rounded-full h-3">
          <div class="bg-green-400 h-3 rounded-full" style="width: 100%"></div>
        </div>
      </div>
      
      <div>
        <div class="flex justify-between text-white/70 mb-2">
          <span>Spending</span>
          <span>₹{monthlySpending}</span>
        </div>
        <div class="w-full bg-white/20 rounded-full h-3">
          <div class="bg-blue-400 h-3 rounded-full" style="width: {(monthlySpending / monthlyBudget) * 100}%"></div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Daily Spending Chart -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Daily Spending This Week</h3>
    <div class="flex items-end justify-between h-48 space-x-2">
      {#each dailySpending as day}
        <div class="flex flex-col items-center flex-1 group">
          <div 
            class="bg-gradient-to-t from-indigo-500 to-purple-500 rounded-t w-full group-hover:from-indigo-400 group-hover:to-purple-400 transition-all duration-300 group-hover:shadow-glow"
            style="height: {(day.amount / 120) * 100}%; min-height: 8px;"
          ></div>
          <span class="text-white/70 text-sm mt-2">{day.day}</span>
          <span class="text-white text-xs font-semibold">₹{day.amount}</span>
        </div>
      {/each}
    </div>
    <div class="mt-4 flex justify-between text-white/60 text-xs">
      <span>Min: ₹25</span>
      <span>Max: ₹120</span>
      <span>Avg: ₹{(dailySpending.reduce((sum, day) => sum + day.amount, 0) / dailySpending.length).toFixed(0)}</span>
    </div>
  </div>
  
  <!-- Enhanced Charts Section -->
  <div class="grid lg:grid-cols-2 gap-6">
    <!-- Category Spending Chart -->
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
        <span class="text-2xl mr-2">📊</span>
        Spending by Category
      </h3>
      <div class="space-y-3">
        {#each categorySpending as item}
          <div class="group">
            <div class="flex justify-between text-white/80 mb-2">
              <span class="font-medium">{item.category}</span>
              <span class="font-bold">₹{item.amount} ({item.percentage}%)</span>
            </div>
            <div class="w-full bg-white/20 rounded-full h-3">
              <div 
                class="bg-gradient-to-r {item.color} h-3 rounded-full group-hover:shadow-glow transition-all duration-300"
                style="width: {item.percentage}%"
              ></div>
            </div>
          </div>
        {/each}
      </div>
    </div>
    
    <!-- Weekly Trend Chart -->
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
        <span class="text-2xl mr-2">📈</span>
        Weekly Spending Trend
      </h3>
      <div class="flex items-end justify-between h-32 space-x-3">
        {#each weeklyTrend as data, index}
          <div class="flex flex-col items-center flex-1 group">
            <div 
              class="bg-gradient-to-t from-blue-500 to-cyan-500 rounded-t w-full group-hover:from-blue-400 group-hover:to-cyan-400 transition-all duration-300 group-hover:shadow-glow"
              style="height: {(data.spending / 3200) * 100}%"
            ></div>
            <span class="text-white/70 text-xs mt-2">{data.week}</span>
            <span class="text-white text-xs font-semibold">₹{data.spending}</span>
          </div>
        {/each}
      </div>
    </div>
  </div>
  
  <!-- Monthly Summary Chart -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
      <span class="text-2xl mr-2">💰</span>
      Monthly Budget Overview
    </h3>
    <div class="grid md:grid-cols-2 gap-6">
      <div>
        <div class="flex justify-between text-white/70 mb-2">
          <span class="font-medium">Budget Utilization</span>
          <span class="font-bold text-cyan-400">{((monthlySpending / monthlyBudget) * 100).toFixed(1)}%</span>
        </div>
        <div class="w-full bg-white/20 rounded-full h-4">
          <div 
            class="bg-gradient-to-r from-green-400 via-yellow-400 to-red-400 h-4 rounded-full"
            style="width: {(monthlySpending / monthlyBudget) * 100}%"
          ></div>
        </div>
        <div class="flex justify-between text-white/60 text-sm mt-2">
          <span>₹{monthlySpending} of ₹{monthlyBudget}</span>
          <span class="text-green-400">₹{monthlyBudget - monthlySpending} left</span>
        </div>
      </div>
      
      <div>
        <div class="text-center">
          <div class="text-4xl font-bold text-white mb-2">
            ₹{monthlyBudget - monthlySpending}
          </div>
          <p class="text-white/70">Remaining Budget</p>
          <div class="mt-4 grid grid-cols-2 gap-4 text-sm">
            <div class="text-center">
              <p class="text-white/60">Daily Average</p>
              <p class="text-white font-semibold">₹{(monthlySpending / 30).toFixed(0)}</p>
            </div>
            <div class="text-center">
              <p class="text-white/60">Days Left</p>
              <p class="text-white font-semibold">8</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Add Expense -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Add New Expense</h3>
    <div class="grid md:grid-cols-4 gap-4">
      <input
        type="text"
        bind:value={newExpense.description}
        placeholder="Description"
        class="px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
      />
      
      <input
        type="number"
        bind:value={newExpense.amount}
        placeholder="Amount"
        class="px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
      />
      
      <select
        bind:value={newExpense.category}
        class="px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
      >
        <option value="food">Food</option>
        <option value="transport">Transport</option>
        <option value="entertainment">Entertainment</option>
        <option value="shopping">Shopping</option>
        <option value="bills">Bills</option>
        <option value="other">Other</option>
      </select>
      
      <button
        on:click={addExpense}
        class="bg-white text-indigo-600 px-4 py-2 rounded-md font-semibold hover:bg-gray-100 transition-colors"
      >
        Add Expense
      </button>
    </div>
  </div>
  
  <!-- Recent Expenses -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
      <span class="text-2xl mr-3">📋</span>
      Recent Expenses
    </h3>
    <div class="space-y-3">
      {#each recentExpenses as expense, index}
        <div class="group p-4 bg-white/5 hover:bg-white/10 rounded-xl border border-white/10 transition-all duration-300">
          <div class="flex items-center justify-between">
            <div class="flex items-center flex-1">
              <div class="w-10 h-10 rounded-lg mr-3 flex items-center justify-center text-lg {
                expense.category === 'food' ? 'bg-gradient-success/20 text-green-400' :
                expense.category === 'transport' ? 'bg-gradient-secondary/20 text-blue-400' :
                expense.category === 'shopping' ? 'bg-gradient-accent/20 text-purple-400' :
                expense.category === 'entertainment' ? 'bg-gradient-warning/20 text-yellow-400' :
                expense.category === 'bills' ? 'bg-gradient-danger/20 text-red-400' :
                'bg-gradient-info/20 text-cyan-400'
              }">
                {expense.category === 'food' ? '🍔' :
                 expense.category === 'transport' ? '🚗' :
                 expense.category === 'shopping' ? '🛍️' :
                 expense.category === 'entertainment' ? '🎬' :
                 expense.category === 'bills' ? '📄' :
                 '📦'}
              </div>
              <div class="flex-1">
                <h4 class="text-white font-semibold">{expense.description}</h4>
                <div class="flex items-center gap-4 mt-1">
                  <span class="px-2 py-1 bg-white/20 text-white text-xs rounded-full capitalize">
                    {expense.category}
                  </span>
                  <span class="text-white/60 text-sm">📅 {expense.date}</span>
                </div>
              </div>
            </div>
            <div class="text-right">
              <span class="text-green-400 font-bold text-lg">₹{expense.amount.toFixed(2)}</span>
            </div>
          </div>
        </div>
      {/each}
    </div>
    {#if recentExpenses.length === 0}
      <p class="text-white/60 text-center py-8">No expenses added yet. Add your first expense above!</p>
    {/if}
  </div>
</div>