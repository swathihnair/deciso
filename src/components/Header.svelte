<script>
  export let showAuthButtons = true;
</script>

<header class="relative bg-gradient-glass backdrop-blur-md border-b border-white/30 shadow-glow">
  <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-20">
      <div class="flex items-center group">
        <div class="w-10 h-10 bg-gradient-aurora rounded-xl mr-3 flex items-center justify-center text-xl group-hover:animate-bounce-slow shadow-aurora relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-shimmer before:opacity-0 hover:before:opacity-50 before:transition-opacity">
          <span class="group-hover:animate-wiggle relative z-10">🎯</span>
        </div>
        <h1 class="text-2xl font-bold text-white group-hover:text-cyan-300 transition-all duration-300 relative">
          Deciso
          <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-cyan-300 to-purple-300 group-hover:w-full transition-all duration-300"></span>
        </h1>
      </div>
      
      {#if showAuthButtons}
        <div class="flex space-x-4">
          <a 
            href="/signin" 
            class="group text-white/90 hover:text-white px-4 py-2 rounded-xl text-sm font-medium transition-all duration-300 hover:bg-gradient-card hover:shadow-glow-cyan relative overflow-hidden before:absolute before:inset-0 before:bg-gradient-aurora before:opacity-0 hover:before:opacity-20 before:transition-opacity"
          >
            <span class="relative z-10">Sign In</span>
          </a>
          <a 
            href="/signup" 
            class="group relative bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 hover:from-blue-700 hover:via-purple-700 hover:to-pink-700 hover:shadow-neon text-white px-6 py-2 rounded-xl text-sm font-bold transition-all duration-300 transform hover:scale-105 overflow-hidden before:absolute before:inset-0 before:bg-gradient-shimmer before:opacity-0 hover:before:opacity-50 before:transition-opacity"
          >
            <span class="relative z-10 flex items-center">
              Sign Up 
              <span class="ml-1 group-hover:animate-wiggle">✨</span>
            </span>
          </a>
        </div>
      {/if}
    </div>
  </nav>
</header>