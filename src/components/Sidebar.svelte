<script>
  export let activeSection = 'dashboard';
  
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: '🏠', gradient: 'from-blue-400 via-cyan-400 to-teal-400' },
    { id: 'financial', label: 'Financial Assistant', icon: '💰', gradient: 'from-green-400 via-emerald-400 to-teal-400' },
    { id: 'style', label: 'Style Assistant', icon: '👗', gradient: 'from-pink-400 via-rose-400 to-red-400' },
    { id: 'goals', label: 'Goals & Planning', icon: '🎯', gradient: 'from-purple-400 via-violet-400 to-indigo-400' },
    { id: 'settings', label: 'Settings', icon: '⚙️', gradient: 'from-gray-400 via-slate-400 to-zinc-400' }
  ];
</script>

<aside class="w-72 bg-gradient-glass backdrop-blur-md border-r border-white/30 min-h-screen shadow-glow relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-mesh before:opacity-20">
  <!-- Logo Section -->
  <div class="p-6 border-b border-white/20">
    <div class="flex items-center group">
      <div class="w-12 h-12 bg-gradient-aurora rounded-2xl mr-4 flex items-center justify-center text-2xl group-hover:animate-bounce-slow shadow-aurora relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-shimmer before:opacity-0 hover:before:opacity-50 before:transition-opacity">
        <span class="group-hover:animate-wiggle relative z-10">🎯</span>
      </div>
      <div>
        <h2 class="text-xl font-bold text-white group-hover:text-cyan-300 transition-all duration-300 relative">
          Deciso
          <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-cyan-300 to-purple-300 group-hover:w-full transition-all duration-300"></span>
        </h2>
        <p class="text-white/70 text-sm">Your Smart Assistant</p>
      </div>
    </div>
  </div>
  
  <!-- Navigation -->
  <nav class="p-6 space-y-3 relative z-10">
    {#each menuItems as item}
      <button
        class="w-full group flex items-center px-4 py-4 text-left rounded-2xl transition-all duration-300 transform hover:scale-105 relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-to-r before:from-transparent before:via-white/10 before:to-transparent before:opacity-0 hover:before:opacity-100 before:transition-opacity before:translate-x-[-100%] hover:before:translate-x-[100%] {
          activeSection === item.id 
            ? 'bg-gradient-hover text-white shadow-glow-strong border border-white/30' 
            : 'text-white/80 hover:bg-gradient-card hover:text-white hover:shadow-glow hover:border hover:border-white/20'
        }"
        on:click={() => activeSection = item.id}
      >
        <div class="w-10 h-10 bg-gradient-to-r {item.gradient} rounded-xl mr-4 flex items-center justify-center text-lg group-hover:animate-pulse shadow-inner-glow relative z-10">
          <span class="group-hover:animate-wiggle">{item.icon}</span>
        </div>
        <div class="flex-1 relative z-10">
          <span class="font-medium">{item.label}</span>
          {#if activeSection === item.id}
            <div class="w-2 h-2 bg-gradient-aurora rounded-full ml-auto animate-pulse-glow shadow-glow-purple"></div>
          {/if}
        </div>
      </button>
    {/each}
  </nav>
  
  <!-- Quick Stats -->
  <div class="px-6 mb-6 relative z-10">
    <div class="bg-gradient-financial/20 backdrop-blur-sm p-4 rounded-2xl border border-white/20 shadow-glow-success relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-financial before:opacity-10">
      <h3 class="text-white font-semibold mb-3 flex items-center relative z-10">
        <span class="text-lg mr-2 animate-pulse-slow">📊</span>
        Today's Progress
      </h3>
      <div class="space-y-2 relative z-10">
        <div class="flex justify-between text-sm">
          <span class="text-white/80">Budget Used</span>
          <span class="text-teal-300 font-semibold animate-pulse-glow">68%</span>
        </div>
        <div class="w-full bg-white/20 rounded-full h-2 relative overflow-hidden">
          <div class="bg-gradient-financial h-2 rounded-full animate-pulse-glow shadow-glow-success" style="width: 68%"></div>
          <div class="absolute inset-0 bg-gradient-shimmer animate-shimmer"></div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- User Profile -->
  <div class="absolute bottom-6 left-6 right-6 z-10">
    <div class="bg-gradient-glass backdrop-blur-sm p-4 rounded-2xl border border-white/30 shadow-glow relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-aurora before:opacity-10">
      <div class="flex items-center relative z-10">
        <div class="w-12 h-12 bg-gradient-dashboard rounded-full mr-3 flex items-center justify-center text-xl animate-pulse-glow shadow-glow relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-shimmer before:opacity-30">
          <span class="animate-wiggle relative z-10">👤</span>
        </div>
        <div class="flex-1">
          <p class="text-white font-semibold">Swathi</p>
          <div class="flex items-center">
            <span class="text-yellow-400 text-xs mr-1 animate-pulse-slow">⭐</span>
            <p class="text-white/70 text-xs">Premium Member</p>
          </div>
        </div>
        <button class="text-white/70 hover:text-white transition-colors group">
          <svg class="w-5 h-5 group-hover:animate-wiggle" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</aside>