import { Component } from 'react'
import axios from 'axios'

import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    loading: true,
    error: false,
    message: ''
  }

  async componentDidMount() {
    let response
    try {
      response = await axios.get('http://localhost:8000')
      this.setState({loading: false, message: response.data})
    } catch (error) {
      console.log(error)
      this.setState({loading: false, error: true})
    }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {this.state.loading ? 'loading' : this.state.error ?
              'There was an error fetching the data' : this.state.message}
          </p>
        </header>
      </div>
    );
  }
}

export default App;
