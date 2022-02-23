import React, {Component} from 'react';
import { Form, Input, InputNumber, Button } from 'antd';
import axios from 'axios';


class CustomForm extends Component {
  constructor(props) {
    super(props);
    this.state = {first_name   : '',
                  last_name    : '',
                  email_id     : '',
                  govt_id      : '',
                  id_no        : '',
                  p_id1        : '',
                  p_id_link    : '',
                  contact      : '',
                  address_1    : '',
                  address_2    : '',
                  city         : '',
                  State        : '',
                  country      : '',
                  zip_code     : '',
                  company_code :''}
    
    
    this.FirstNamehandleChange   = this.FirstNamehandleChange.bind(this);
    this.LastNamehandleChange    = this.LastNamehandleChange.bind(this);
    this.EmailhandleChange       = this.EmailhandleChange.bind(this);
    this.GovthandleChange        = this.GovthandleChange.bind(this);
    this.IDhandleChange          = this.IDhandleChange.bind(this);
    this.PIDhandleChange         = this.PIDhandleChange.bind(this);
    this.PLINKhandleChange       = this.PLINKhandleChange.bind(this);
    this.ContacthandleChange     = this.ContacthandleChange.bind(this);
    this.ADD1handleChange        = this.ADD1handleChange.bind(this);
    this.ADD2handleChange        = this.ADD2handleChange.bind(this);
    this.CityhandleChange        = this.CityhandleChange.bind(this);
    this.StatehandleChange       = this.StatehandleChange.bind(this);
    this.CountryhandleChange     = this.CountryhandleChange.bind(this);
    this.ZiphandleChange         = this.ZiphandleChange.bind(this);
    this.CompanyhandleChange     = this.CompanyhandleChange.bind(this);
    this.handleSubmitForm        = this.handleSubmitForm.bind(this);
  }

  FirstNamehandleChange(event) {
    this.setState({first_name: event.target.value,
    });
  }
  LastNamehandleChange(event) {
    this.setState({last_name: event.target.value,
    });
  }
  EmailhandleChange(event) {
    this.setState({email_id: event.target.value,
    });
  }
  GovthandleChange(event) {
    this.setState({govt_id: event.target.value,
    });
  }
  IDhandleChange(event) {
    this.setState({id_no: event.target.value,
    });
  }
  PIDhandleChange(event) {
    this.setState({p_id1: event.target.value,
    });
  }
  PLINKhandleChange(event) {
    this.setState({p_id_link: event.target.value,
    });
  }
  ContacthandleChange(event) {
    this.setState({contact: event.target.value,
    });
  }
  ADD1handleChange(event) {
    this.setState({address_1: event.target.value,
    });
  }
  ADD2handleChange(event) {
    this.setState({address_2: event.target.value,
    });
  }
  CityhandleChange(event) {
    this.setState({city: event.target.value,
    });
  }
  StatehandleChange(event) {
    this.setState({State: event.target.value,
    });
  }
  CountryhandleChange(event) {
    this.setState({country: event.target.value,
    });
  }
  ZiphandleChange(event) {
    this.setState({zip_code: event.target.value,
    });
  }
  CompanyhandleChange(event) {
    this.setState({company_code: event.target.value,
    });
  }
  handleSubmitForm = (event,requestType,articleID) => {
      event.preventDefault()
      const first_name   = this.state.first_name
      const last_name    = this.state.last_name
      const email_id     = this.state.email_id
      const govt_id      = this.state.govt_id
      const id_no        = this.state.id_no
      const p_id1        = this.state.p_id1
      const p_id_link    = this.state.p_id_link
      const contact      = this.state.contact
      const address_1    = this.state.address_1
      const address_2    = this.state.address_2
      const city         = this.state.city
      const State        = this.state.State
      const country      = this.state.country
      const zip_code     = this.state.zip_code
      const company_code = this.state.company_code
      
      console.log(first_name)
      console.log('vikas')
      const body1 = {
                        first_name   : first_name, 
                        last_name    : last_name,
                        email_id     : email_id,
                        govt_id      : govt_id,
                        id_no        : id_no,
                        p_id1        : p_id1,
                        p_id_link    : p_id_link,
                        contact      : contact,
                        address_1    : address_1,
                        address_2    : address_2,
                        city         : city,
                        state        : State,
                        country      : country,
                        zip_code     : zip_code,
                        company_code : company_code
                      }
      switch (requestType) {
        case 'post':
            return axios.post('http://127.0.0.1:8000/api/auth/customer/',body1)
            .then(res => console.log(res))
            .catch(error => console.log(error))

          case 'put':
              return axios.put(`http://127.0.0.1:8000/api/auth/customer/${articleID}/`,body1)
              .then(res => console.log(res))
              .catch(error => console.log(error))
      }
  }
  render(){
    return (
        <div>
            <Form>
                <Form.Item label="First Name">
                    <Input 
                    // name='first_name' 
                    value={this.state.first_name} 
                    onChange={this.FirstNamehandleChange}
                    placeholder="Write First Name"/>
                </Form.Item>
                <Form.Item label="Last Name">
                <Input  
                    // name='first_name' 
                    value={this.state.last_name} 
                    onChange={this.LastNamehandleChange}
                    placeholder="Write last Name"/>
                </Form.Item>
                <Form.Item label="Email ID">
                <Input  
                    // name='first_name' 
                    value={this.state.email_id} 
                    onChange={this.EmailhandleChange}
                    placeholder="Write Your First Name"/>
                </Form.Item>
                <Form.Item label="Govt ID">
                <Input  
                    // name='first_name' 
                    value={this.state.govt_id} 
                    onChange={this.GovthandleChange}
                    placeholder="Write govt.id"/>
                </Form.Item>
                <Form.Item label="">
                <Input 
                    // name='first_name' 
                    value={this.state.id_no} 
                    onChange={this.IDhandleChange}
                    placeholder="put id number"/>
                </Form.Item>
                <Form.Item label="Personal ID">
                <Input  
                    // name='first_name' 
                    value={this.state.p_id1} 
                    onChange={this.PIDhandleChange}
                    placeholder="put personal id"/>
                </Form.Item>
                <Form.Item label="">
                <Input 
                    // name='first_name' 
                    value={this.state.p_id_link} 
                    onChange={this.PLINKhandleChange}
                    placeholder="Write contact"/>
                </Form.Item>
                <Form.Item label="Contact">
                <Input 
                    // name='first_name' 
                    value={this.state.contact} 
                    onChange={this.ContacthandleChange}
                    placeholder="Write contact"/>
                </Form.Item>
                <Form.Item label="Address 1 ">
                <Input  
                    // name='first_name' 
                    value={this.state.address_1} 
                    onChange={this.ADD1handleChange}
                    placeholder="Write address_1 "/>
                </Form.Item>
                <Form.Item label="Address 2 ">
                <Input  
                    // name='first_name' 
                    value={this.state.address_2} 
                    onChange={this.ADD2handleChange}
                    placeholder="Write address_2 "/>
                </Form.Item>
                <Form.Item label="City">
                <Input  
                    // name='first_name' 
                    value={this.state.city} 
                    onChange={this.CityhandleChange}
                    placeholder="Write city"/>
                </Form.Item>
                <Form.Item label="State">
                <Input 
                    // name='first_name' 
                    value={this.state.State} 
                    onChange={this.StatehandleChange}
                    placeholder="Write state"/>
                </Form.Item>
                <Form.Item label="Country">
                <Input 
                    // name='first_name' 
                    value={this.state.country} 
                    onChange={this.CountryhandleChange}
                    placeholder="Write country"/>
                </Form.Item>
                <Form.Item label="Zip Code">
                <Input 
                    // name='first_name' 
                    value={this.state.zip_code} 
                    onChange={this.ZiphandleChange}
                    placeholder="Write zip code"/>
                </Form.Item>
                <Form.Item label="Company Code">
                <Input 
                    // name='first_name' 
                    value={this.state.company_code} 
                    onChange={this.CompanyhandleChange}
                    placeholder="Write company code"/>
                </Form.Item>
                <Form.Item >
                    <Button className='primary' onClick={(event) => this.handleSubmitForm(
                            event,
                            this.props.requestType,
                            this.props.articleID)}
                            htmlType="submit">{this.props.btnTxt}
                            
                    </Button>
                </Form.Item>
            </Form>
        </div>
        
    );
  };
};

export default CustomForm;
