<script>
  let currentTime = new Date().toLocaleTimeString();
  let userName = "John";
  
  // Update time every second
  setInterval(() => {
    currentTime = new Date().toLocaleTimeString();
  }, 1000);
  
  const quickStats = [
    { label: 'Budget Remaining', value: '$800', color: 'from-green-400 to-emerald-500', icon: '💰', trend: '+12%' },
    { label: 'Outfits Planned', value: '5', color: 'from-pink-400 to-rose-500', icon: '👗', trend: '+2' },
    { label: 'Goals Completed', value: '3/7', color: 'from-yellow-400 to-orange-500', icon: '🎯', trend: '43%' },
    { label: 'Decisions Made', value: '12', color: 'from-indigo-400 to-purple-500', icon: '✅', trend: '+8' }
  ];
  
  const recentActivities = [
    { action: 'Added expense: Lunch at Cafe Luna', time: '2 hours ago', type: 'financial', amount: '$24.50' },
    { action: 'Saved outfit for Friday interview', time: '4 hours ago', type: 'style', amount: null },
    { action: 'Completed goal: Morning workout', time: '1 day ago', type: 'goal', amount: null },
    { action: 'Updated budget for groceries', time: '2 days ago', type: 'financial', amount: '$150' }
  ];
  
  const upcomingTasks = [
    { task: 'Review monthly budget', due: 'Today', priority: 'high', icon: '💰' },
    { task: 'Plan outfit for Friday meeting', due: 'Tomorrow', priority: 'medium', icon: '👗' },
    { task: 'Update savings goal', due: 'This week', priority: 'low', icon: '🎯' }
  ];
</script>

<div class="space-y-8 animate-fade-in">
  <!-- Welcome Header -->
  <div class="bg-gradient-card backdrop-blur-md p-8 rounded-3xl border border-white/20 shadow-glass relative overflow-hidden">
    <!-- Decorative elements -->
    <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-accent/20 rounded-full blur-2xl"></div>
    <div class="absolute bottom-0 left-0 w-24 h-24 bg-gradient-success/20 rounded-full blur-xl"></div>
    
    <div class="relative flex justify-between items-center">
      <div class="animate-slide-up">
        <h1 class="text-4xl font-bold text-white mb-2">
          Welcome back, <span class="text-cyan-300">{userName}</span>! 
          <span class="animate-bounce-slow inline-block">👋</span>
        </h1>
        <p class="text-white/80 text-lg">Here's what's happening with your decisions today</p>
      </div>
      <div class="text-right animate-scale-in">
        <p class="text-white/70 text-sm mb-1">Current Time</p>
        <p class="text-white font-bold text-2xl bg-gradient-card px-4 py-2 rounded-xl border border-white/20">
          {currentTime}
        </p>
      </div>
    </div>
  </div>
  
  <!-- Quick Stats -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
    {#each quickStats as stat, index}
      <div class="group bg-gradient-card backdrop-blur-md p-6 rounded-2xl border border-white/20 hover:bg-gradient-hover transition-all duration-500 transform hover:scale-105 hover:shadow-glow animate-slide-up" style="animation-delay: {index * 0.1}s;">
        <div class="flex items-center justify-between mb-4">
          <div class="text-3xl group-hover:animate-bounce-slow">{stat.icon}</div>
          <div class="text-right">
            <div class="text-xs text-green-400 font-semibold bg-green-400/20 px-2 py-1 rounded-full">
              {stat.trend}
            </div>
          </div>
        </div>
        <h3 class="text-white/80 text-sm font-medium mb-2">{stat.label}</h3>
        <p class="text-3xl font-bold text-white mb-2">{stat.value}</p>
        <div class="w-full bg-white/20 rounded-full h-2">
          <div class="bg-gradient-to-r {stat.color} h-2 rounded-full animate-pulse" style="width: {Math.random() * 40 + 60}%"></div>
        </div>
      </div>
    {/each}
  </div>
  
  <!-- Main Content Grid -->
  <div class="grid lg:grid-cols-3 gap-8">
    <!-- Recent Activities -->
    <div class="lg:col-span-2 bg-gradient-card backdrop-blur-md p-8 rounded-3xl border border-white/20 shadow-glass animate-slide-up">
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-2xl font-bold text-white flex items-center">
          <span class="text-3xl mr-3">📈</span>
          Recent Activities
        </h2>
        <button class="text-white/60 hover:text-white transition-colors text-sm font-medium">
          View All
        </button>
      </div>
      <div class="space-y-4">
        {#each recentActivities as activity, index}
          <div class="group flex items-center p-4 bg-gradient-card hover:bg-gradient-hover rounded-2xl border border-white/10 transition-all duration-300 hover:shadow-card animate-scale-in" style="animation-delay: {index * 0.1}s;">
            <div class="w-12 h-12 rounded-2xl mr-4 flex items-center justify-center text-xl {
              activity.type === 'financial' ? 'bg-gradient-success/20 text-green-400' :
              activity.type === 'style' ? 'bg-gradient-secondary/20 text-pink-400' :
              'bg-gradient-accent/20 text-blue-400'
            } group-hover:animate-pulse">
              {activity.type === 'financial' ? '💰' : activity.type === 'style' ? '👗' : '🎯'}
            </div>
            <div class="flex-1">
              <p class="text-white font-semibold mb-1">{activity.action}</p>
              <div class="flex items-center justify-between">
                <p class="text-white/60 text-sm">{activity.time}</p>
                {#if activity.amount}
                  <span class="text-green-400 font-bold text-sm">{activity.amount}</span>
                {/if}
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
    
    <!-- Upcoming Tasks -->
    <div class="bg-gradient-card backdrop-blur-md p-8 rounded-3xl border border-white/20 shadow-glass animate-slide-up" style="animation-delay: 0.2s;">
      <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
        <span class="text-3xl mr-3">⏰</span>
        Upcoming Tasks
      </h2>
      <div class="space-y-4">
        {#each upcomingTasks as task, index}
          <div class="group p-4 bg-gradient-card hover:bg-gradient-hover rounded-2xl border border-white/10 transition-all duration-300 hover:shadow-card animate-scale-in" style="animation-delay: {index * 0.1}s;">
            <div class="flex items-center justify-between mb-3">
              <div class="text-2xl group-hover:animate-bounce-slow">{task.icon}</div>
              <span class="text-xs px-3 py-1 rounded-full font-semibold {
                task.priority === 'high' ? 'bg-red-500/20 text-red-400' :
                task.priority === 'medium' ? 'bg-yellow-500/20 text-yellow-400' :
                'bg-green-500/20 text-green-400'
              }">
                {task.priority}
              </span>
            </div>
            <p class="text-white font-semibold text-sm mb-2">{task.task}</p>
            <p class="text-white/60 text-xs">Due: {task.due}</p>
          </div>
        {/each}
      </div>
      
      <button
        class="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-2xl font-bold transition-all duration-300 transform hover:scale-105"
      >
        View All Tasks
      </button>
    </div>
  </div>
  
  <!-- Quick Actions -->
  <div class="bg-gradient-card backdrop-blur-md p-8 rounded-3xl border border-white/20 shadow-glass animate-slide-up" style="animation-delay: 0.3s;">
    <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
      <span class="text-3xl mr-3">⚡</span>
      Quick Actions
    </h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <button class="group p-6 bg-gray-800 hover:bg-gray-700 rounded-2xl border border-white/10 transition-all duration-300 hover:shadow-glow transform hover:scale-105 text-center">
        <div class="text-4xl mb-3 group-hover:animate-bounce-slow">💰</div>
        <p class="text-white text-sm font-semibold">Add Expense</p>
      </button>
      
      <button class="group p-6 bg-gray-800 hover:bg-gray-700 rounded-2xl border border-white/10 transition-all duration-300 hover:shadow-glow transform hover:scale-105 text-center">
        <div class="text-4xl mb-3 group-hover:animate-bounce-slow">👗</div>
        <p class="text-white text-sm font-semibold">Plan Outfit</p>
      </button>
      
      <button class="group p-6 bg-gray-800 hover:bg-gray-700 rounded-2xl border border-white/10 transition-all duration-300 hover:shadow-glow transform hover:scale-105 text-center">
        <div class="text-4xl mb-3 group-hover:animate-bounce-slow">🎯</div>
        <p class="text-white text-sm font-semibold">Set Goal</p>
      </button>
      
      <button class="group p-6 bg-gray-800 hover:bg-gray-700 rounded-2xl border border-white/10 transition-all duration-300 hover:shadow-glow transform hover:scale-105 text-center">
        <div class="text-4xl mb-3 group-hover:animate-bounce-slow">📊</div>
        <p class="text-white text-sm font-semibold">View Reports</p>
      </button>
    </div>
  </div>
</div>