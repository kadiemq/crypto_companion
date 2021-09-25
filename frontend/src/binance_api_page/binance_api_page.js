import React, {useState} from "react";
import './style.css'
import axios from "axios";
import {useC} from "../utils/context";
import {Redirect, useHistory} from "react-router-dom";

const BinanceApiPage = () => {

    const {haveApi, systemMsg} = useC()
    let history = useHistory();

    const [, setHaveApi] = haveApi
    const [, setSystemMsg] = systemMsg

    const [publicApi, setPublicApi] = useState('')
    const [secretApi, setSecretApi] = useState('')

    const handle_submit = (e) => {
        e.preventDefault();

        const data = {'binance_public_api': publicApi,'binance_secret_api': secretApi}

        axios.patch('', data, {withCredentials: true})
            .then((r) => {
                setHaveApi(true)
                setSystemMsg('Updated Api')
                history.push("/portfolio")
            })
            .catch((e) => console.log(e))
    }
    return (
        <section className={'binance_api_section'}>

            <div className={'binance_api_form_div'}>
                <p>Update Binance Api</p>
                <form onSubmit={handle_submit} className={'binance_api_form'}>
                    <input type={'text'} placeholder={'Public Api'} value={publicApi} onChange={(e) => setPublicApi(e.target.value)}/>
                    <input type={'password'} placeholder={'Secret Api'} value={secretApi} onChange={(e) => setSecretApi(e.target.value)}/>
                    <input type="submit" value="Submit"/>
                </form>

            </div>

        </section>
    )
}

export default BinanceApiPage;
