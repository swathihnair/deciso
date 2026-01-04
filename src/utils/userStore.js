// Simple user data store
export let userData = {
  fullName: '',
  email: '',
  isLoggedIn: false
};

// Load user data from localStorage on page load
if (typeof window !== 'undefined') {
  const savedData = localStorage.getItem('userData');
  if (savedData) {
    userData = JSON.parse(savedData);
  }
}

// Function to update user data
export function updateUserData(data) {
  userData = { ...userData, ...data, isLoggedIn: true };
  if (typeof window !== 'undefined') {
    localStorage.setItem('userData', JSON.stringify(userData));
  }
}

// Function to clear user data (logout)
export function clearUserData() {
  userData = { fullName: '', email: '', isLoggedIn: false };
  if (typeof window !== 'undefined') {
    localStorage.removeItem('userData');
  }
}
