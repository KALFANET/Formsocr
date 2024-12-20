import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import ProcessForm from './pages/ProcessForm';

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/process" element={<ProcessForm />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
