import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Home from './pages/Home'
import Restaurant from './pages/Restaurant';
import ProfileQuestions from './pages/ProfileQuestions';
import SearchQuestions from './pages/SearchQuestions';
import CreateAccount from './pages/CreateAccount';
import Login from './pages/Login';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/createaccount" element={<CreateAccount />} />
          <Route path="/createprofile" element={<ProfileQuestions />} />
          <Route path="/searchquestions" element={<SearchQuestions />} />
          <Route path="/restaurantsearch" element={<Restaurant />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
