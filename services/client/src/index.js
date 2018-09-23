import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';


class App extends Component {
    constructor(){
	super();
	this.state = {
	    users: []
	};
    }
    componentDidMount(){
	this.getUsers();
    };
    render(){
	return(
	    <section className="section">
	    <div className="container">
		<div className="columns">
		<div className="column is-half">
		<br/>
	    <h1 className="title is1 is1">All Users</h1>
		<hr/><br/>
		<AddUser/>
		<hr/><br/>
		<UsersList users={this.state.users}/>
	    </div>
	    </div>
	    </div>
	    </section>
	)
    }
    getUsers(){
	axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
	    .then((res) => { this.setState({users: res.data.data.users}); })
	    .catch((err) => { console.log(err); });
    }
};

ReactDOM.render(
	<App />,
	document.getElementById('root')
);
