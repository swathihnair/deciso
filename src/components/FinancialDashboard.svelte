<script>
  let dailySpending = [
    { day: 'Mon', amount: 45 },
    { day: 'Tue', amount: 32 },
    { day: 'Wed', amount: 78 },
    { day: 'Thu', amount: 25 },
    { day: 'Fri', amount: 95 },
    { day: 'Sat', amount: 120 },
    { day: 'Sun', amount: 60 }
  ];
  
  let monthlyBudget = 4000;
  let monthlySpending = 3200;
  let newExpense = { description: '', amount: '', category: 'food' };
  
  // Additional chart data
  let categorySpending = [
    { category: 'Food', amount: 850, percentage: 26.5, color: 'from-green-400 to-emerald-500' },
    { category: 'Transport', amount: 450, percentage: 14, color: 'from-blue-400 to-cyan-500' },
    { category: 'Shopping', amount: 680, percentage: 21.2, color: 'from-purple-400 to-pink-500' },
    { category: 'Entertainment', amount: 320, percentage: 10, color: 'from-yellow-400 to-orange-500' },
    { category: 'Bills', amount: 900, percentage: 28.1, color: 'from-red-400 to-rose-500' }
  ];
  
  let weeklyTrend = [
    { week: 'Week 1', spending: 2800 },
    { week: 'Week 2', spending: 3100 },
    { week: 'Week 3', spending: 2900 },
    { week: 'Week 4', spending: 3200 }
  ];
  
  function addExpense() {
    if (newExpense.description && newExpense.amount) {
      // Add expense logic here
      console.log('Adding expense:', newExpense);
      
      // Update daily spending (add to today)
      const today = dailySpending[dailySpending.length - 1];
      today.amount += parseFloat(newExpense.amount);
      
      // Update monthly spending
      monthlySpending += parseFloat(newExpense.amount);
      
      // Reset form
      newExpense = { description: '', amount: '', category: 'food' };
      
      // Show success message
      alert('Expense added successfully!');
    } else {
      alert('Please fill in all fields');
    }
  }
</script>

<div class="space-y-6">
  <h2 class="text-2xl font-bold text-white">Financial Assistant</h2>
  
  <!-- Budget Overview -->
  <div class="grid md:grid-cols-3 gap-6">
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Monthly Budget</h3>
      <p class="text-3xl font-bold text-green-400">₹{monthlyBudget}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Spent This Month</h3>
      <p class="text-3xl font-bold text-blue-400">₹{monthlySpending}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Remaining</h3>
      <p class="text-3xl font-bold text-purple-400">₹{monthlyBudget - monthlySpending}</p>
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
    <div class="flex items-end justify-between h-40 space-x-2">
      {#each dailySpending as day}
        <div class="flex flex-col items-center flex-1">
          <div 
            class="bg-gradient-to-t from-indigo-500 to-purple-500 rounded-t w-full"
            style="height: {(day.amount / 120) * 100}%"
          ></div>
          <span class="text-white/70 text-sm mt-2">{day.day}</span>
          <span class="text-white text-xs">₹{day.amount}</span>
        </div>
      {/each}
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
</div>