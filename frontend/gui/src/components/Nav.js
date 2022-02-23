import React, { Component } from 'react';
import { Link } from 'react-router-dom';
class Nav extends Component {
    render() {
        return (

            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <a className="navbar-brand" href="/"><span className="fas fa-plus-circle"></span>&nbsp; CRM -></a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>
            
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item active">
                        <a className="nav-link text-white text-uppercase" href='/profile'>Profiles</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link text-white text-uppercase" href=''>Finance</a>
                        </li>  
                        <li className="nav-item">
                            <a className="nav-link text-white text-uppercase" href="">HR</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link text-white text-uppercase" href="">Payroll</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link text-white text-uppercase" href="">ProjectManagement</a>
                        </li>
                        <li className="nav-item ">
                            <a className="nav-link text-white text-uppercase" href="">Service</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link text-white text-uppercase" href="">Sla</a>
                        </li>
                        <li className="nav-item">
                        <Link className='nav-link text-white text-uppercase' to = '/about'>About</Link>
                        </li>
                        
                    </ul>
                    {/* <form className="form-inline my-2 my-lg-0">
                        <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form> */}
                    

                </div>
            </nav>
        )
    }
}

export default Nav;


