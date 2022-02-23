// import React from 'react';
// import { List, Avatar, Space } from 'antd';

import React, { Component } from 'react';

class Article extends Component {
  render() {
    return this.props.data.map((todo) => (
      <div>
        <h2>
        <a href={`/${todo.id}`}>{todo.first_name}</a>
        <br/>
        </h2>
        <li>lastname      : {todo.last_name}</li>
        <li>email_id      : {todo.email_id}</li>
        <li>govt_id       : {todo.govt_id}</li>
        <li>id_no         : {todo.id_no}</li>
        <li>p_id1         : {todo.p_id1}</li>
        <li>p_id_link     : {todo.p_id_link}</li>
        <li>contact       : {todo.contact}</li>
        <li>address_1     : {todo.address_1}</li>
        <li>address_2     : {todo.address_2}</li>
        <li>city          : {todo.city}</li>
        <li>state         : {todo.state}</li>
        <li>country       : {todo.country}</li>
        <li>zip_code      : {todo.zip_code}</li>
        <li>company_code  : {todo.company_code}</li>
        <li>customer_id   : {todo.customer_id}</li>
        <br/>
      </div>
      
      
    ));
    
  }
}

export default Article;



