import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Home from './pages/Home'
import Restaurant from './pages/Restaurant';
import ProfileQuestions from './pages/ProfileQuestions';
import NewProfileQuestions from './pages/NewProfileQuestions';
import NewSearchQuestions from './pages/NewSearchQuestions';
import SearchQuestions from './pages/SearchQuestions';
import CreateAccount from './pages/CreateAccount';
import Login from './pages/Login';
import EditAccount from './pages/EditAccount';
import Dashboard  from './pages/Dashboard';
import Group  from './pages/Group';
import JoinGroup  from './pages/JoinGroup';
import GroupSearchQuestions  from './pages/GroupSearchQuestions';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/createaccount" element={<CreateAccount />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/edit/account" element={<EditAccount />} />
          <Route path="/edit/preferences" element={<NewProfileQuestions />} />
          <Route path="/newsearchquestions" element={<NewSearchQuestions />} />
          <Route path="/searchquestions" element={<SearchQuestions />} />
          <Route path="/restaurantsearch" element={<Restaurant />} />
          <Route path="/group" element={<Group />} />
          <Route path="/join/group/:host" element={<JoinGroup />} />
          <Route path="/group/searchquestions" element={<GroupSearchQuestions />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
