import React from 'react'; 
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';

import { AppBar, Footer } from './base';

class App extends React.Component {
  render() {
    return (
      <React.Fragment>
        <Router>
           <AppBar />
     		      <BaseRouter />
           <Footer />
        </Router>
      </React.Fragment>
    );
  }
}

export default App;
