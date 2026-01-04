<script>
  let settings = {
    notifications: {
      email: true,
      push: false,
      budgetAlerts: true,
      styleReminders: true
    },
    privacy: {
      profileVisibility: 'private',
      dataSharing: false,
      analytics: true
    },
    preferences: {
      theme: 'gradient',
      currency: 'USD',
      language: 'en',
      timezone: 'America/New_York'
    }
  };
  
  function saveSettings() {
    console.log('Saving settings:', settings);
    // Here you would typically send the settings to your backend
  }
</script>

<div class="space-y-6">
  <h2 class="text-2xl font-bold text-white">Settings</h2>
  
  <!-- Profile Settings -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Profile Information</h3>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <label for="fullName" class="block text-sm font-medium text-white mb-2">Full Name</label>
        <input
          type="text"
          id="fullName"
          value="Swathi"
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
        />
      </div>
      
      <div>
        <label for="email" class="block text-sm font-medium text-white mb-2">Email</label>
        <input
          type="email"
          id="email"
          value="swathi@example.com"
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
        />
      </div>
      
      <div>
        <label for="phone" class="block text-sm font-medium text-white mb-2">Phone Number</label>
        <input
          type="tel"
          id="phone"
          value="+1 (555) 123-4567"
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
        />
      </div>
      
      <div>
        <label for="location" class="block text-sm font-medium text-white mb-2">Location</label>
        <input
          type="text"
          id="location"
          value="New York, NY"
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
        />
      </div>
    </div>
  </div>
  
  <!-- Notification Settings -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Notifications</h3>
    <div class="space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-white font-medium">Email Notifications</p>
          <p class="text-white/60 text-sm">Receive updates via email</p>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" bind:checked={settings.notifications.email} class="sr-only peer">
          <div class="w-11 h-6 bg-white/20 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
        </label>
      </div>
      
      <div class="flex items-center justify-between">
        <div>
          <p class="text-white font-medium">Push Notifications</p>
          <p class="text-white/60 text-sm">Receive push notifications on your device</p>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" bind:checked={settings.notifications.push} class="sr-only peer">
          <div class="w-11 h-6 bg-white/20 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
        </label>
      </div>
      
      <div class="flex items-center justify-between">
        <div>
          <p class="text-white font-medium">Budget Alerts</p>
          <p class="text-white/60 text-sm">Get notified when approaching budget limits</p>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" bind:checked={settings.notifications.budgetAlerts} class="sr-only peer">
          <div class="w-11 h-6 bg-white/20 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
        </label>
      </div>
      
      <div class="flex items-center justify-between">
        <div>
          <p class="text-white font-medium">Style Reminders</p>
          <p class="text-white/60 text-sm">Reminders to plan outfits for upcoming events</p>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" bind:checked={settings.notifications.styleReminders} class="sr-only peer">
          <div class="w-11 h-6 bg-white/20 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
        </label>
      </div>
    </div>
  </div>
  
  <!-- Preferences -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Preferences</h3>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <label for="currency" class="block text-sm font-medium text-white mb-2">Currency</label>
        <select
          id="currency"
          bind:value={settings.preferences.currency}
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
        >
          <option value="USD">USD ($)</option>
          <option value="EUR">EUR (€)</option>
          <option value="GBP">GBP (£)</option>
          <option value="JPY">JPY (¥)</option>
        </select>
      </div>
      
      <div>
        <label for="language" class="block text-sm font-medium text-white mb-2">Language</label>
        <select
          id="language"
          bind:value={settings.preferences.language}
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
        >
          <option value="en">English</option>
          <option value="es">Spanish</option>
          <option value="fr">French</option>
          <option value="de">German</option>
        </select>
      </div>
      
      <div>
        <label for="timezone" class="block text-sm font-medium text-white mb-2">Timezone</label>
        <select
          id="timezone"
          bind:value={settings.preferences.timezone}
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
        >
          <option value="America/New_York">Eastern Time</option>
          <option value="America/Chicago">Central Time</option>
          <option value="America/Denver">Mountain Time</option>
          <option value="America/Los_Angeles">Pacific Time</option>
        </select>
      </div>
      
      <div>
        <label for="theme" class="block text-sm font-medium text-white mb-2">Theme</label>
        <select
          id="theme"
          bind:value={settings.preferences.theme}
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
        >
          <option value="gradient">Gradient (Current)</option>
          <option value="dark">Dark Mode</option>
          <option value="light">Light Mode</option>
        </select>
      </div>
    </div>
  </div>
  
  <!-- Privacy Settings -->
  <div class="bg-white/10 backdrop-blur-md p-6 rounded-xl border border-white/20">
    <h3 class="text-lg font-semibold text-white mb-4">Privacy & Security</h3>
    <div class="space-y-4">
      <div>
        <label for="profileVisibility" class="block text-sm font-medium text-white mb-2">Profile Visibility</label>
        <select
          id="profileVisibility"
          bind:value={settings.privacy.profileVisibility}
          class="w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-white/50"
        >
          <option value="private">Private</option>
          <option value="friends">Friends Only</option>
          <option value="public">Public</option>
        </select>
      </div>
      
      <div class="flex items-center justify-between">
        <div>
          <p class="text-white font-medium">Data Sharing</p>
          <p class="text-white/60 text-sm">Allow sharing anonymized data for improvements</p>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" bind:checked={settings.privacy.dataSharing} class="sr-only peer">
          <div class="w-11 h-6 bg-white/20 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
        </label>
      </div>
      
      <div class="flex items-center justify-between">
        <div>
          <p class="text-white font-medium">Analytics</p>
          <p class="text-white/60 text-sm">Help us improve by sharing usage analytics</p>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" bind:checked={settings.privacy.analytics} class="sr-only peer">
          <div class="w-11 h-6 bg-white/20 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
        </label>
      </div>
    </div>
  </div>
  
  <!-- Save Button -->
  <div class="flex justify-end">
    <button
      on:click={saveSettings}
      class="bg-white text-indigo-600 px-6 py-2 rounded-md font-semibold hover:bg-gray-100 transition-colors"
    >
      Save Changes
    </button>
  </div>
</div>
