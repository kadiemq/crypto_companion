import React, {useState} from "react";
import './style.css'
import logo from '../logo.png'
import axios from 'axios'
import {Link} from "react-router-dom";
import {useC} from "../utils/context";
import {useHistory,useLocation} from "react-router-dom";

const LoginPage = () => {
    const [usernameForm, setUsernameForm] = useState('')
    const [password, setPassword] = useState('')

    const {isAuthenticated, username, haveApi, systemMsg} = useC()


    const [, setIsAuthenticated] = isAuthenticated
    const [, setUsername] = username
    const [, setHaveApi] = haveApi
    const [, setSystemMsg] = systemMsg


    const handle_submit = (e) => {
        e.preventDefault();

        const data = {username: usernameForm, password}

        axios.post('', data, {withCredentials: true})
            .then((r) => {
                const user = r.data.user
                const haveApi = r.data.setup_api
                setUsername(user)
                setHaveApi(haveApi)
                setSystemMsg('Logged in')
                setIsAuthenticated(true)
            })
            .catch((e) => console.log(e))
    }
    return (
        <section className={'login_section'}>

            <div className={'login_form_div'}>
                <p>Login</p>
                <form onSubmit={handle_submit} className={'login_form'}>
                    <input type={'text'} placeholder={'Username'} value={usernameForm} onChange={(e) => setUsernameForm(e.target.value)}/>
                    <input type={'password'} placeholder={'Password'} value={password} onChange={(e) => setPassword(e.target.value)}/>
                    <input type="submit" value="Submit"/>
                </form>
                <Link to={'/signup'}><span>Create account</span></Link>

            </div>

        </section>
    )
}

export default LoginPage
