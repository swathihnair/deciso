/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f9ff',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        }
      },
      backgroundImage: {
        // Main background gradients
        'gradient-primary': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'gradient-main': 'linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%)',
        'gradient-dark': 'linear-gradient(135deg, #1a1a2e 0%, #3a2e4e 100%)',
        'gradient-darker': 'linear-gradient(135deg, #000000 0%, #0d1117 25%, #161b22 50%, #21262d 75%, #30363d 100%)',

        // Card and component gradients
        'gradient-card': 'linear-gradient(145deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.03) 100%)',
        'gradient-hover': 'linear-gradient(145deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.06) 100%)',
        'gradient-glass': 'linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%)',

        // Accent gradients
        'gradient-accent': 'linear-gradient(135deg, #ff6b6b 0%, #ff8e53 25%, #ff6b9d 50%, #c44569 75%, #f8b500 100%)',
        'gradient-accent-alt': 'linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%)',
        'gradient-rainbow': 'linear-gradient(135deg, #667eea 0%, #764ba2 16%, #f093fb 32%, #f5576c 48%, #4facfe 64%, #00f2fe 80%, #43e97b 100%)',
        'gradient-rainbow-dark': 'linear-gradient(135deg, #4c63d2 0%, #5a4b8c 16%, #d63384 32%, #dc3545 48%, #0dcaf0 64%, #20c997 80%, #198754 100%)',

        // Specific color gradients
        'gradient-success': 'linear-gradient(135deg, #0d7377 0%, #2d9596 100%)',
        'gradient-success-alt': 'linear-gradient(135deg, #1e40af 0%, #3730a3 100%)',
        'gradient-warning': 'linear-gradient(135deg, #dc2626 0%, #b91c1c 100%)',
        'gradient-warning-alt': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
        'gradient-error': 'linear-gradient(135deg, #dc2626 0%, #b91c1c 100%)',
        'gradient-info': 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)',

        // Financial gradients
        'gradient-financial': 'linear-gradient(135deg, #0d7377 0%, #2d9596 50%, #1e40af 100%)',
        'gradient-expense': 'linear-gradient(135deg, #dc2626 0%, #f59e0b 100%)',
        'gradient-income': 'linear-gradient(135deg, #059669 0%, #0d7377 100%)',

        // Style gradients
        'gradient-style': 'linear-gradient(135deg, #dc2626 0%, #f59e0b 50%, #3b82f6 100%)',
        'gradient-fashion': 'linear-gradient(135deg, #3b82f6 0%, #7c3aed 50%, #dc2626 100%)',

        // Dashboard gradients
        'gradient-dashboard': 'linear-gradient(135deg, #3b82f6 0%, #7c3aed 25%, #dc2626 50%, #f59e0b 75%, #059669 100%)',
        'gradient-stats': 'linear-gradient(135deg, #0d7377 0%, #2d9596 25%, #1e40af 50%, #3730a3 75%, #3b82f6 100%)',

        // Special effects
        'gradient-glow': 'radial-gradient(circle, rgba(59, 130, 246, 0.3) 0%, rgba(124, 58, 237, 0.15) 50%, transparent 100%)',
        'gradient-glow-strong': 'radial-gradient(circle, rgba(59, 130, 246, 0.4) 0%, rgba(124, 58, 237, 0.25) 50%, transparent 100%)',
        'gradient-shimmer': 'linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.3) 50%, transparent 70%)',
        'gradient-mesh': 'radial-gradient(at 40% 20%, hsla(280,100%,74%,0.3) 0px, transparent 50%), radial-gradient(at 80% 0%, hsla(189,100%,56%,0.3) 0px, transparent 50%), radial-gradient(at 0% 50%, hsla(355,100%,93%,0.3) 0px, transparent 50%)',
        'gradient-aurora': 'linear-gradient(135deg, rgba(120, 119, 198, 0.3), rgba(255, 119, 198, 0.3), rgba(255, 206, 84, 0.3), rgba(120, 219, 255, 0.3))',
        'gradient-neon': 'linear-gradient(135deg, #00ff88, #00bbff, #ff00ff, #ff0088)',
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'float-delayed': 'float 8s ease-in-out infinite',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'pulse-glow': 'pulseGlow 2s ease-in-out infinite alternate',
        'bounce-slow': 'bounce 2s infinite',
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'slide-down': 'slideDown 0.5s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
        'shimmer': 'shimmer 2s linear infinite',
        'gradient-shift': 'gradientShift 3s ease-in-out infinite',
        'rotate-slow': 'rotate 20s linear infinite',
        'wiggle': 'wiggle 1s ease-in-out infinite',
        'glow-pulse': 'glowPulse 2s ease-in-out infinite',
        'morph': 'morph 4s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        pulseGlow: {
          '0%': { boxShadow: '0 0 20px rgba(102, 126, 234, 0.3)' },
          '100%': { boxShadow: '0 0 30px rgba(102, 126, 234, 0.6)' },
        },
        shimmer: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(100%)' },
        },
        gradientShift: {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
        wiggle: {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
        glowPulse: {
          '0%, 100%': { opacity: '0.6', transform: 'scale(1)' },
          '50%': { opacity: '1', transform: 'scale(1.05)' },
        },
        morph: {
          '0%, 100%': { borderRadius: '60% 40% 30% 70% / 60% 30% 70% 40%' },
          '50%': { borderRadius: '30% 60% 70% 40% / 50% 60% 30% 60%' },
        },
      },
      boxShadow: {
        'glass': '0 8px 32px 0 rgba(0, 0, 0, 0.5)',
        'glow': '0 0 20px rgba(59, 130, 246, 0.4)',
        'glow-strong': '0 0 30px rgba(59, 130, 246, 0.6)',
        'glow-accent': '0 0 25px rgba(220, 38, 38, 0.4)',
        'glow-success': '0 0 25px rgba(13, 115, 119, 0.4)',
        'glow-warning': '0 0 25px rgba(220, 38, 38, 0.4)',
        'glow-purple': '0 0 25px rgba(124, 58, 237, 0.4)',
        'glow-pink': '0 0 25px rgba(236, 72, 153, 0.4)',
        'glow-cyan': '0 0 25px rgba(6, 182, 212, 0.4)',
        'card': '0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2)',
        'card-hover': '0 20px 40px -10px rgba(0, 0, 0, 0.4), 0 15px 20px -5px rgba(0, 0, 0, 0.3)',
        'inner-glow': 'inset 0 2px 4px 0 rgba(255, 255, 255, 0.05)',
        'neon': '0 0 10px rgba(59, 130, 246, 0.8), 0 0 20px rgba(59, 130, 246, 0.6), 0 0 30px rgba(59, 130, 246, 0.4)',
        'aurora': '0 0 20px rgba(120, 119, 198, 0.4), 0 0 40px rgba(255, 119, 198, 0.3), 0 0 60px rgba(255, 206, 84, 0.2)',
      },
      backdropBlur: {
        'xs': '2px',
      }
    },
  },
  plugins: [require('@tailwindcss/forms')],
}