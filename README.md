# Deciso - Personalized Decision Making Assistant

A beautiful, personalized web application that helps users make better decisions about their finances, style choices, and daily life. Built with Astro, Svelte, Tailwind CSS, and Flask.

## Features

- **Personalized Dashboard**: Beautiful, gradient-themed interface with real-time updates
- **Financial Assistant**: Track expenses, manage budgets, and visualize spending patterns
- **Style Assistant**: Get outfit recommendations for any occasion (interviews, festivals, casual, etc.)
- **User Authentication**: Secure sign-up and sign-in system
- **Personalization**: Comprehensive onboarding to tailor the experience
- **Responsive Design**: Works perfectly on desktop and mobile devices

## Tech Stack

### Frontend
- **Astro**: Modern static site generator
- **Svelte**: Reactive component framework
- **Tailwind CSS**: Utility-first CSS framework
- **Gradient Theme**: Beautiful indigo-purple gradient design

### Backend
- **Python Flask**: Lightweight web framework
- **SQLite**: Database for user data and preferences
- **Flask-CORS**: Cross-origin resource sharing

## Project Structure

```
decision-maker-app/
├── src/
│   ├── components/
│   │   ├── Header.svelte
│   │   ├── Sidebar.svelte
│   │   ├── MainDashboard.svelte
│   │   ├── FinancialDashboard.svelte
│   │   ├── StyleAssistant.svelte
│   │   └── Settings.svelte
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       ├── index.astro (Landing page)
│       ├── signin.astro
│       ├── signup.astro
│       ├── personalize.astro
│       └── dashboard.astro
├── backend/
│   ├── app.py (Flask application)
│   └── requirements.txt
├── package.json
├── astro.config.mjs
└── tailwind.config.mjs
```

## Getting Started

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Frontend Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:4321`

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Start the Flask server:
```bash
python app.py
```

The backend API will be available at `http://localhost:5000`

## User Flow

1. **Landing Page**: Welcome page with features and testimonials
2. **Sign Up**: User registration with email and password
3. **Personalization**: Comprehensive form to collect user preferences:
   - Personal information (age, occupation, location)
   - Financial goals and budget
   - Style preferences and body type
   - Interests and lifestyle
4. **Dashboard**: Main interface with sidebar navigation:
   - **Dashboard**: Overview with quick stats and recent activities
   - **Financial Assistant**: Budget tracking, expense management, charts
   - **Style Assistant**: Outfit recommendations based on occasion and weather
   - **Goals & Planning**: Personal goal tracking (coming soon)
   - **Settings**: User preferences and account management

## Key Features

### Financial Assistant
- Monthly budget vs spending visualization
- Daily spending charts
- Expense categorization
- Budget alerts and insights
- Add expenses with categories

### Style Assistant
- Occasion-based outfit recommendations
- Weather-appropriate suggestions
- Style tips and advice
- Multiple occasions: casual, work, interview, date, party, festival, wedding, gym

### Personalization
- Comprehensive user profiling
- Tailored recommendations
- Adaptive interface based on preferences
- Goal-oriented suggestions

## API Endpoints

- `POST /api/register` - User registration
- `POST /api/login` - User authentication
- `POST /api/profile` - Save user profile data
- `POST /api/expenses` - Add new expense
- `GET /api/expenses` - Get user expenses
- `GET /api/dashboard-stats` - Get dashboard statistics
- `POST /api/logout` - User logout

## Design Features

- **Gradient Theme**: Beautiful indigo-purple gradients throughout
- **Glass Morphism**: Frosted glass effects with backdrop blur
- **Responsive Design**: Mobile-first approach
- **Interactive Elements**: Smooth transitions and hover effects
- **Accessibility**: Proper contrast ratios and semantic HTML

## Development Notes

- The application uses static generation for optimal performance
- Svelte components are hydrated on the client for interactivity
- The backend uses SQLite for simplicity but can be upgraded to PostgreSQL
- All forms include proper validation and error handling
- The design system is consistent throughout the application

## Future Enhancements

- Goals & Planning module
- Advanced analytics and insights
- Social features and sharing
- Mobile app development
- AI-powered recommendations
- Integration with shopping platforms
- Calendar integration for outfit planning

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.