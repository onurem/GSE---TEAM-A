import logo from './logo.svg';
import './App.css';
import { Routes, Route, Outlet, Link } from "react-router-dom";
import Dashboard from './components/Dashboard';
import MainView from './dashboard_views/MainView';
import DemoForm from './components/DemoForm';

import { useState } from 'react';
import AuthProvider, { RequireAuth } from './components/AuthProvider';
import SignInSide from './components/SignIn';


function App() {
  return (
    <div className="App">
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<SignInSide />} />
          <Route path="/" element={<RequireAuth><Dashboard /></RequireAuth>}>
            <Route index element={<MainView />} />
            <Route path="/demo" element={<DemoForm />} />
          </Route>
          {/* <Route
            path="/"
            element={<RequireAuth>
              <Route index element={<Dashboard />}>
                <Route path="/" element={<MainView />} />
              </Route>
            </RequireAuth>} /> */}
        </Routes>
      </AuthProvider>
    </div>
  );
}

export default App;
