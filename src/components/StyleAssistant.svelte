<script>
  let selectedOccasion = 'casual';
  let weatherCondition = 'mild';
  let recommendations = [];
  
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
  
  function getRecommendations() {
    // Mock recommendations based on occasion
    const mockRecommendations = {
      casual: [
        { item: 'Comfortable Jeans', color: 'Dark Blue', brand: 'Levi\'s' },
        { item: 'Cotton T-Shirt', color: 'White', brand: 'Uniqlo' },
        { item: 'Sneakers', color: 'White', brand: 'Adidas' }
      ],
      work: [
        { item: 'Dress Shirt', color: 'Light Blue', brand: 'Brooks Brothers' },
        { item: 'Chinos', color: 'Navy', brand: 'Banana Republic' },
        { item: 'Dress Shoes', color: 'Brown', brand: 'Cole Haan' }
      ],
      interview: [
        { item: 'Suit Jacket', color: 'Charcoal', brand: 'Hugo Boss' },
        { item: 'Dress Pants', color: 'Charcoal', brand: 'Hugo Boss' },
        { item: 'Dress Shirt', color: 'White', brand: 'Calvin Klein' },
        { item: 'Tie', color: 'Navy Blue', brand: 'Hermès' }
      ],
      festival: [
        { item: 'Bohemian Top', color: 'Floral Print', brand: 'Free People' },
        { item: 'High-waisted Shorts', color: 'Denim', brand: 'Urban Outfitters' },
        { item: 'Ankle Boots', color: 'Brown', brand: 'Dr. Martens' },
        { item: 'Crossbody Bag', color: 'Tan', brand: 'Coach' }
      ]
    };
    
    recommendations = mockRecommendations[selectedOccasion] || mockRecommendations.casual;
  }
  
  // Get initial recommendations
  getRecommendations();
</script>

<div class="space-y-6">
  <h2 class="text-2xl font-bold text-white">Style Assistant</h2>
  
  <!-- Occasion Selection -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Choose Your Occasion</h3>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
      {#each occasions as occasion}
        <button
          class="p-4 rounded-lg border transition-colors {
            selectedOccasion === occasion.id 
              ? 'bg-white/20 border-white/40 text-white' 
              : 'bg-white/5 border-white/20 text-white/70 hover:bg-white/10'
          }"
          on:click={() => {
            selectedOccasion = occasion.id;
            getRecommendations();
          }}
        >
          <div class="text-2xl mb-2">{occasion.icon}</div>
          <div class="text-sm font-medium">{occasion.label}</div>
        </button>
      {/each}
    </div>
  </div>
  
  <!-- Weather & Preferences -->
  <div class="grid md:grid-cols-2 gap-6">
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4">Weather Condition</h3>
      <select
        bind:value={weatherCondition}
        on:change={getRecommendations}
        class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
      >
        <option value="hot">Hot (80°F+)</option>
        <option value="mild">Mild (60-80°F)</option>
        <option value="cool">Cool (40-60°F)</option>
        <option value="cold">Cold (Below 40°F)</option>
      </select>
    </div>
    
    <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
      <h3 class="text-lg font-semibold text-white mb-4">Style Preference</h3>
      <div class="space-y-2">
        <label class="flex items-center text-white/70">
          <input type="radio" name="style" value="conservative" class="mr-2">
          Conservative
        </label>
        <label class="flex items-center text-white/70">
          <input type="radio" name="style" value="trendy" class="mr-2" checked>
          Trendy
        </label>
        <label class="flex items-center text-white/70">
          <input type="radio" name="style" value="bold" class="mr-2">
          Bold & Unique
        </label>
      </div>
    </div>
  </div>
  
  <!-- Outfit Recommendations -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">
      Recommended Outfit for {occasions.find(o => o.id === selectedOccasion)?.label}
    </h3>
    
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
      {#each recommendations as item}
        <div class="bg-white/10 p-4 rounded-lg border border-white/20">
          <h4 class="font-semibold text-white mb-2">{item.item}</h4>
          <p class="text-white/70 text-sm mb-1">Color: {item.color}</p>
          <p class="text-white/70 text-sm mb-3">Brand: {item.brand}</p>
          <button class="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-4 rounded-md text-sm font-medium transition-colors">
            View Similar Items
          </button>
        </div>
      {/each}
    </div>
  </div>
  
  <!-- Style Tips -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Style Tips</h3>
    <div class="space-y-3">
      <div class="flex items-start">
        <span class="text-yellow-400 mr-3">💡</span>
        <p class="text-white/70">
          {#if selectedOccasion === 'interview'}
            Keep colors neutral and professional. Avoid flashy patterns or accessories.
          {:else if selectedOccasion === 'festival'}
            Don't be afraid to mix patterns and textures. Comfort is key for long days.
          {:else if selectedOccasion === 'casual'}
            Layer pieces for versatility. A light jacket can elevate any casual look.
          {:else}
            Choose pieces that make you feel confident and comfortable.
          {/if}
        </p>
      </div>
      
      <div class="flex items-start">
        <span class="text-green-400 mr-3">✨</span>
        <p class="text-white/70">
          Accessories can transform any outfit. Consider adding a watch, belt, or statement jewelry.
        </p>
      </div>
      
      <div class="flex items-start">
        <span class="text-blue-400 mr-3">👗</span>
        <p class="text-white/70">
          Fit is everything. Well-fitted clothes always look more expensive and polished.
        </p>
      </div>
    </div>
  </div>
</div>