import React from 'react';
import ArticleList from './containers/ArticleListView';
import Finance from './components/modules/finance/Finance';
import Profile from './components/modules/profile/Profiles';
import Hr from './components/modules/hr/Hr'
import Service from './components/modules/service/Service'
import Payroll from './components/modules/payroll/Payroll'
import Sla from './components/modules/sla/Sla'
import Projectmanagement from './components/modules/projectmanagement/Projectmanagement'
import ArticleDetail from './containers/ArticleDetailView';
import HomePage from './components/HomePage';
import AboutPage from './components/AboutPage';
import { Route ,Switch} from 'react-router-dom';  

const BaseRoute = () => (
    <div>
        <Switch>
            <Route exact path='/' component={HomePage}/>
            <Route exact path='/finance' component={Finance}/>
            <Route exact path='/profile' component={ArticleList}/>
            <Route exact path='/hr' component={Hr}/>
            <Route exact path='/service' component={Service}/>
            <Route exact path='/payroll' component={Payroll}/>
            <Route exact path='/sla' component={Sla}/>
            <Route exact path='/project' component={Projectmanagement}/>
            <Route exact path='/about' component={AboutPage}/>
            <Route exact path='/:articleID' component={ArticleDetail}/>            
        </Switch>
        
    </div>
        
    
)



export default BaseRoute;

// for now just dealing with path "/" and "/:articleID" and "/profile"