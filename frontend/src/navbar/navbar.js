import React from "react";
import './style.css'
import {useC} from "../utils/context";
import {Link} from "react-router-dom";
import axios from "axios";

const Navbar = () => {

    const {isAuthenticated, username, haveApi, systemMsg} = useC()

    const [isAuthenticatedValue, setIsAuthenticated] = isAuthenticated
    const [usernameValue, setUsername] = username
    const [haveApiValue, setHaveApi] = haveApi
    const [systemMsgValue] = systemMsg

    const handle_logout = (e) => {
        e.preventDefault();

        axios.get('', {withCredentials: true})
            .then((r) => {
                setUsername(null)
                setHaveApi(false)
                setIsAuthenticated(false)
            })
            .catch((e) => console.log(e))
    }

    return (
        <section className={'navbar_section'}>
            <div className={'navbar_div'}>

                <div className="navbar_welcome_msg_div">
                    <p>Hello, {isAuthenticatedValue? usernameValue:'Anonymous'}</p>
                </div>

                <div className="navbar_navigation_div">
                    <Link to={'/'}><span>Home</span></Link>
                    <Link to={'/news'}><span>News</span></Link>
                    <Link to={'/portfolio'}><span>Portfolio</span></Link>
                    <Link to={'/alerts'}><span>Alerts</span></Link>
                </div>

                <div className="navbar_auth_div">
                    {isAuthenticatedValue? <button onClick={handle_logout}>Logout</button>: <Link to={'/login'}><span>Login</span></Link>}
                </div>

            </div>
            <p className={'navbar_system_msg'}>{systemMsgValue}</p>
        </section>
    )
}

export default Navbar;
