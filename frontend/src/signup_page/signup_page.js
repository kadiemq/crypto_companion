import React, {useState} from "react";
import './style.css'
import {useC} from "../utils/context";
import axios from "axios";
import logo from "../logo.png";
import {Link} from "react-router-dom";

const SignupPage = () => {

    const {systemMsg} = useC()
    const [, setSystemMsg] = systemMsg

    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [email, setEmail] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')


    const handle_submit = (e) => {
        e.preventDefault();

        const data = {username, password, email, last_name, first_name}

        axios.post('', data, {withCredentials: true})
            .then((r) => {
                setSystemMsg('Registered a new account successfully')
                console.log(r.data)
            })
            .catch((error) => {
                if (error.response) {
                    console.log(error.response.data);
                } else if (error.request) {
                    console.log(error.request);
                } else {
                    console.log('Error', error.message);
                }
            })
    }
    return (
        <section className={'signup_section'}>

            <div className={'signup_form_div'}>
                <p>Signup</p>
                <form onSubmit={handle_submit} className={'signup_form'}>
                    <input type={'text'} placeholder={'First Name'} value={first_name} onChange={(e) => setFirstName(e.target.value)}/>
                    <input type={'text'} placeholder={'Last Name'} value={last_name} onChange={(e) => setLastName(e.target.value)}/>
                    <input type={'text'} placeholder={'email'} value={email} onChange={(e) => setEmail(e.target.value)}/>
                    <input type={'text'} placeholder={'Username'} value={username} onChange={(e) => setUsername(e.target.value)}/>
                    <input type={'password'} placeholder={'Password'} value={password} onChange={(e) => setPassword(e.target.value)}/>
                    <input type="submit" value="Submit"/>
                </form>
                <Link to={'/login'}><span>Already have account</span></Link>

            </div>

        </section>
    )
}

export default SignupPage
