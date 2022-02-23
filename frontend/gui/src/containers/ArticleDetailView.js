import React, { Component } from 'react';
import Article from '../components/Article';
import axios from 'axios';
import { Button } from 'antd'
import CustomForm from '../components/Form';

class ArticleDetail extends Component {
    state = {
        articles: []
    }

    componentDidMount() {
        const articleID = this.props.match.params.articleID
        axios.get(`http://127.0.0.1:8000/api/auth/customer/${articleID}/`).then(
            res => {this.setState({articles: [res.data]});
            console.log(this.state.articles)}
        )
        
    }
    handleDelete = (event) => {
        // event.preventDefault()
        
        const articleID = this.props.match.params.articleID
        axios.delete(`http://127.0.0.1:8000/api/auth/customer/${articleID}/`)
        this.props.history.push('/')
        this.forceUpdate()
        
    }
    render() {
        return (
            <div>
                <Article data={this.state.articles} 
                articleID={this.props.match.params.articleID}/>
                <h2>Update User</h2>
                <CustomForm 
                requestType='put'
                articleID={this.props.match.params.articleID}
                btnTxt='Update'/>
                <form>
                    <Button onClick={(event) => this.handleDelete(event)} type='danger' htmlType='submit'>Delete</Button>
                </form>
            </div>
            
        )
    }
}

export default ArticleDetail;

