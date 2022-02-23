import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css';
import CustomLayout from './containers/layout';
// import Article from './components/Article';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRoute from './routes';
import Nav from './components/Nav'
class App extends Component {

  render() {
    return (
      <div>
        <Router>
          <CustomLayout>
             {/* <Nav/> */}
             <BaseRoute />
          </CustomLayout>
          
        </Router>
      </div>
    )
  }
}

export default App;


