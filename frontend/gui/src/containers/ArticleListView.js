import React, { Component } from 'react';
import Article from '../components/Article';
import axios from 'axios';
import CustomForm from '../components/Form';



class ArticleList extends Component {
    state = {
        articles: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/auth/customer/').then(
            res => {this.setState({articles: res.data});
            console.log(res.data)}
        )
        
    }
    render() {
        return (
            <div>
                <Article data={this.state.articles}/>
                <br/>
                <h2>Add An User</h2>
                <CustomForm 
                requestType='post'
                articleID={null}
                btnTxt='Create'/>
            </div>
            
        )
    }
}

export default ArticleList;
