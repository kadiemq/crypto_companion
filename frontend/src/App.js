import './App.css';
import React, {useEffect} from "react";
import {BrowserRouter, Route, Switch} from "react-router-dom";

import LoadingPage from "./loading_page/loading_page";
import HomePage from "./home_page/home_page";
import NewsPage from "./news_page/news_page";
import PortfolioPage from "./portfolio_page/portfolio_page";
import AlertsPage from "./alerts_page/alerts_page";
import BinanceApiPage from "./binance_api_page/binance_api_page";
import LoginPage from "./login_page/login_page";
import SignupPage from "./signup_page/signup_page";
import AuthenticatedOnly from "./utils/authenticated_only_route";
import UnauthenticatedOnly from "./utils/unauthenticated_only_route";
import axios from "axios";
import {useC} from "./utils/context";
import Navbar from "./navbar/navbar";
import NewAlertPage from "./new_alert_page/new_alert";

function App() {

    const {isAuthenticated, username, haveApi} = useC()
    const [isAuthenticatedValue, setIsAuthenticated] = isAuthenticated
    const [usernameValue, setUsername] = username
    const [haveApiValue, setHaveApi] = haveApi

    useEffect(() => {
        axios.get('', {withCredentials: true})
            .then((r) => {
                const user = r.data.user
                const haveApi = r.data.setup_api
                setUsername(user)
                setHaveApi(haveApi === 'true')
                setIsAuthenticated(true)
            })
            .catch((e) => console.log(e))
    }, [])

  return (
          <BrowserRouter>

              <Navbar />
              <LoadingPage />

              <Switch>
                  <Route path={'/'} component={HomePage} exact/>
                  <Route path={'/news'} component={NewsPage} exact/>

                  <UnauthenticatedOnly path={'/login'}>
                      <LoginPage />
                  </UnauthenticatedOnly>

                  <UnauthenticatedOnly path={'/signup'}>
                      <SignupPage />
                  </UnauthenticatedOnly>

                  <AuthenticatedOnly path={'/binance_api'}>
                      <BinanceApiPage />
                  </AuthenticatedOnly>

                  <AuthenticatedOnly path={'/portfolio'}>
                      <PortfolioPage />
                  </AuthenticatedOnly>

                  <AuthenticatedOnly path={'/alerts'}>
                      <AlertsPage />
                  </AuthenticatedOnly>

                  <AuthenticatedOnly path={'/new_alert'}>
                      <NewAlertPage />
                  </AuthenticatedOnly>

              </Switch>
          </BrowserRouter>
  );
}

export default App;
