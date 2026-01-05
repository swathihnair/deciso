<script>
  import { onMount } from 'svelte';
  
  let selectedOccasion = 'casual';
  let weatherCondition = 'mild';
  let budget = 5000;
  let travelDistance = 'local';
  let stylePreference = 'trendy';
  let recommendations = [];
  let styleTip = '';
  let isLoading = false;
  let recommendationSource = '';
  let userProfile = null;
  
  const occasions = [
    { id: 'casual', label: 'Casual Day Out', icon: '👕' },
    { id: 'work', label: 'Work/Office', icon: '👔' },
    { id: 'interview', label: 'Job Interview', icon: '💼' },
    { id: 'date', label: 'Date Night', icon: '💕' },
    { id: 'party', label: 'Party/Event', icon: '🎉' },
    { id: 'festival', label: 'Festival', icon: '🎪' },
    { id: 'wedding', label: 'Wedding', icon: '💒' },
    { id: 'gym', label: 'Gym/Workout', icon: '💪' }
  ];
  
  const travelOptions = [
    { id: 'local', label: 'Local (< 30 mins)' },
    { id: 'nearby', label: 'Nearby City (1-2 hours)' },
    { id: 'outstation', label: 'Outstation (3+ hours)' },
    { id: 'flight', label: 'Flight Travel' }
  ];

  // Load user profile from localStorage
  function loadUserProfile() {
    const storedProfile = localStorage.getItem('userProfile');
    if (storedProfile) {
      userProfile = JSON.parse(storedProfile);
      if (userProfile.monthlyBudget) {
        budget = Math.min(userProfile.monthlyBudget * 0.1, 10000); // 10% of monthly budget or max 10k
      }
    }
  }
  
  async function getRecommendations() {
    isLoading = true;
    recommendations = [];
    
    try {
      const response = await fetch('http://localhost:5000/api/outfit-recommendation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          occasion: selectedOccasion,
          budget: budget,
          weather: weatherCondition,
          travelDistance: travelDistance,
          stylePreference: stylePreference
        })
      });
      
      if (response.ok) {
        const data = await response.json();
        recommendations = data.recommendations || [];
        styleTip = data.style_tip || '';
        recommendationSource = data.source || 'unknown';
      } else {
        // Use fallback on error
        recommendations = getFallbackRecommendations();
        styleTip = 'Choose pieces that make you feel confident and comfortable.';
        recommendationSource = 'fallback';
      }
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      // Use fallback on network error
      recommendations = getFallbackRecommendations();
      styleTip = 'Choose pieces that make you feel confident and comfortable.';
      recommendationSource = 'fallback';
    }
    
    isLoading = false;
  }
  
  function getFallbackRecommendations() {
    const fallback = {
      casual: [
        { item: 'Cotton T-Shirt', color: 'White', price: budget * 0.2, tip: 'A wardrobe essential' },
        { item: 'Comfortable Jeans', color: 'Dark Blue', price: budget * 0.35, tip: 'Choose slim fit' },
        { item: 'Canvas Sneakers', color: 'White', price: budget * 0.3, tip: 'Keep them clean' },
        { item: 'Casual Watch', color: 'Brown', price: budget * 0.15, tip: 'Adds sophistication' }
      ],
      wedding: [
        { item: 'Silk Kurta Set', color: 'Royal Blue', price: budget * 0.4, tip: 'Pair with gold mojaris' },
        { item: 'Embroidered Stole', color: 'Gold', price: budget * 0.15, tip: 'Drape elegantly' },
        { item: 'Ethnic Mojaris', color: 'Gold/Tan', price: budget * 0.25, tip: 'Break them in first' },
        { item: 'Statement Watch', color: 'Gold Tone', price: budget * 0.2, tip: 'Classic accessory' }
      ],
      work: [
        { item: 'Formal Shirt', color: 'Light Blue', price: budget * 0.25, tip: 'Ensure proper fit' },
        { item: 'Formal Trousers', color: 'Navy', price: budget * 0.3, tip: 'Get them tailored' },
        { item: 'Leather Belt', color: 'Brown', price: budget * 0.15, tip: 'Match with shoes' },
        { item: 'Oxford Shoes', color: 'Brown', price: budget * 0.3, tip: 'Polish regularly' }
      ]
    };
    return fallback[selectedOccasion] || fallback.casual;
  }
  
  onMount(() => {
    loadUserProfile();
    getRecommendations();
  });
</script>

<div class="space-y-6">
  <h2 class="text-2xl font-bold text-white">Style Assistant</h2>
  
  <!-- AI Badge -->
  <div class="flex items-center gap-2">
    <span class="px-3 py-1 bg-gradient-to-r from-purple-500 to-pink-500 text-white text-sm rounded-full flex items-center">
      <span class="mr-2">✨</span>
      Powered by Gemini AI
    </span>
    {#if recommendationSource === 'gemini'}
      <span class="px-2 py-1 bg-green-500/20 text-green-400 text-xs rounded-full">AI Active</span>
    {:else if recommendationSource === 'fallback'}
      <span class="px-2 py-1 bg-yellow-500/20 text-yellow-400 text-xs rounded-full">Curated Picks</span>
    {/if}
  </div>
  
  <!-- Occasion Selection -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Choose Your Occasion</h3>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
      {#each occasions as occasion}
        <button
          class="p-4 rounded-lg border transition-all duration-300 transform hover:scale-105 {
            selectedOccasion === occasion.id 
              ? 'bg-gradient-to-r from-purple-500/30 to-pink-500/30 border-purple-400/50 text-white shadow-lg' 
              : 'bg-white/5 border-white/20 text-white/70 hover:bg-white/10'
          }"
          on:click={() => {
            selectedOccasion = occasion.id;
          }}
        >
          <div class="text-2xl mb-2">{occasion.icon}</div>
          <div class="text-sm font-medium">{occasion.label}</div>
        </button>
      {/each}
    </div>
  </div>
  
  <!-- Budget, Weather & Travel -->
  <div class="grid md:grid-cols-3 gap-6">
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4">💰 Budget (₹)</h3>
      <input
        type="number"
        bind:value={budget}
        min="500"
        max="100000"
        step="500"
        class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-purple-500/50"
      />
      <input
        type="range"
        bind:value={budget}
        min="500"
        max="50000"
        step="500"
        class="w-full mt-3 accent-purple-500"
      />
      <p class="text-white/60 text-sm mt-2">₹{budget.toLocaleString()}</p>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4">🌤️ Weather</h3>
      <select
        bind:value={weatherCondition}
        class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-purple-500/50"
      >
        <option value="hot">Hot (35°C+)</option>
        <option value="warm">Warm (25-35°C)</option>
        <option value="mild">Mild (15-25°C)</option>
        <option value="cool">Cool (5-15°C)</option>
        <option value="cold">Cold (Below 5°C)</option>
        <option value="rainy">Rainy</option>
      </select>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4">🚗 Travel Distance</h3>
      <select
        bind:value={travelDistance}
        class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-purple-500/50"
      >
        {#each travelOptions as option}
          <option value={option.id}>{option.label}</option>
        {/each}
      </select>
    </div>
  </div>
  
  <!-- Style Preference -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Style Preference</h3>
    <div class="flex flex-wrap gap-3">
      {#each ['conservative', 'classic', 'trendy', 'bold', 'minimalist'] as style}
        <button
          class="px-4 py-2 rounded-full border transition-all duration-300 {
            stylePreference === style
              ? 'bg-purple-500/30 border-purple-400 text-white'
              : 'bg-white/5 border-white/20 text-white/70 hover:bg-white/10'
          }"
          on:click={() => stylePreference = style}
        >
          {style.charAt(0).toUpperCase() + style.slice(1)}
        </button>
      {/each}
    </div>
  </div>
  
  <!-- Get Recommendations Button -->
  <button
    on:click={getRecommendations}
    disabled={isLoading}
    class="w-full bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white py-4 px-6 rounded-xl font-semibold transition-all duration-300 transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
  >
    {#if isLoading}
      <span class="animate-spin">⏳</span>
      Getting AI Recommendations...
    {:else}
      <span>✨</span>
      Get AI Outfit Recommendations
    {/if}
  </button>
  
  <!-- Outfit Recommendations -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
      <span>👗</span>
      Recommended Outfit for {occasions.find(o => o.id === selectedOccasion)?.label}
      <span class="text-sm font-normal text-white/60">(Budget: ₹{budget.toLocaleString()})</span>
    </h3>
    
    {#if isLoading}
      <div class="flex items-center justify-center py-12">
        <div class="animate-pulse flex flex-col items-center">
          <div class="text-4xl mb-4 animate-bounce">🤖</div>
          <p class="text-white/70">AI is curating your perfect outfit...</p>
        </div>
      </div>
    {:else}
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        {#each recommendations as item, index}
          <div class="bg-gradient-to-br from-white/10 to-white/5 p-4 rounded-xl border border-white/20 hover:border-purple-400/50 transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
            <div class="text-3xl mb-3 text-center">
              {index === 0 ? '👔' : index === 1 ? '👖' : index === 2 ? '👟' : '⌚'}
            </div>
            <h4 class="font-semibold text-white mb-2 text-center">{item.item}</h4>
            <div class="space-y-1 text-sm">
              <p class="text-white/70 flex justify-between">
                <span>Color:</span>
                <span class="text-purple-300">{item.color}</span>
              </p>
              <p class="text-white/70 flex justify-between">
                <span>Price:</span>
                <span class="text-green-400 font-semibold">₹{Math.round(item.price).toLocaleString()}</span>
              </p>
            </div>
            <div class="mt-3 p-2 bg-white/5 rounded-lg">
              <p class="text-white/60 text-xs">💡 {item.tip}</p>
            </div>
          </div>
        {/each}
      </div>
      
      <!-- Total Budget -->
      {#if recommendations.length > 0}
        <div class="mt-6 p-4 bg-gradient-to-r from-green-500/20 to-emerald-500/20 rounded-xl border border-green-500/30">
          <div class="flex justify-between items-center">
            <span class="text-white font-medium">Estimated Total:</span>
            <span class="text-2xl font-bold text-green-400">
              ₹{Math.round(recommendations.reduce((sum, item) => sum + item.price, 0)).toLocaleString()}
            </span>
          </div>
          <p class="text-white/60 text-sm mt-1">
            {recommendations.reduce((sum, item) => sum + item.price, 0) <= budget 
              ? '✅ Within your budget!' 
              : '⚠️ Slightly over budget - consider alternatives'}
          </p>
        </div>
      {/if}
    {/if}
  </div>
  
  <!-- Style Tips -->
  {#if styleTip}
    <div class="bg-gradient-to-r from-purple-500/20 to-pink-500/20 backdrop-blur-md p-6 rounded-xl border border-purple-500/30">
      <h3 class="text-lg font-semibold text-white mb-3 flex items-center gap-2">
        <span>💡</span>
        AI Style Tip
      </h3>
      <p class="text-white/80">{styleTip}</p>
    </div>
  {/if}
</div>
