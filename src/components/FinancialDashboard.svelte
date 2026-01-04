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
  
  function addExpense() {
    if (newExpense.description && newExpense.amount) {
      // Add expense logic here
      console.log('Adding expense:', newExpense);
      newExpense = { description: '', amount: '', category: 'food' };
    }
  }
</script>

<div class="space-y-6">
  <h2 class="text-2xl font-bold text-white">Financial Assistant</h2>
  
  <!-- Budget Overview -->
  <div class="grid md:grid-cols-3 gap-6">
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Monthly Budget</h3>
      <p class="text-3xl font-bold text-green-400">${monthlyBudget}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Spent This Month</h3>
      <p class="text-3xl font-bold text-blue-400">${monthlySpending}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-2">Remaining</h3>
      <p class="text-3xl font-bold text-purple-400">${monthlyBudget - monthlySpending}</p>
    </div>
  </div>
  
  <!-- Budget vs Spending Chart -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Budget vs Spending</h3>
    <div class="space-y-4">
      <div>
        <div class="flex justify-between text-white/70 mb-2">
          <span>Budget</span>
          <span>${monthlyBudget}</span>
        </div>
        <div class="w-full bg-white/20 rounded-full h-3">
          <div class="bg-green-400 h-3 rounded-full" style="width: 100%"></div>
        </div>
      </div>
      
      <div>
        <div class="flex justify-between text-white/70 mb-2">
          <span>Spending</span>
          <span>${monthlySpending}</span>
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
          <span class="text-white text-xs">${day.amount}</span>
        </div>
      {/each}
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