import './style.css'
import React, {useState} from "react";
import {useC} from "../utils/context";
import axios from "axios";

const NewAlertPage = () => {

    const {systemMsg} = useC()
    const [, setSystemMsg] = systemMsg

    const [symbol, setSymbol] = useState('')
    const [direction, setDirection] = useState('ABOVE')
    const [trigger, setTrigger] = useState('')
    const [message, setMessage] = useState('')

    const data = {
        "type": "NA",
        "symbol": symbol,
        "order_type": "NA",
        "time_in_force": "NA",
        "trigger": trigger,
        "price": trigger,
        "quantity": 0,
        "direction": direction,
        "notify": ['email'],
        "action": "NA",
        "message": message,
        "done": false
    }

    const handle_submit = (e) => {
        e.preventDefault();
        axios.post('', data, {withCredentials: true})
            .then((r) => {
                setSystemMsg('Alert successfully created')
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
        <section className={'new_alert_section'}>

            <div className="new_alert_div">

                <form onSubmit={handle_submit}>

                    <input type={'text'} placeholder={'Symbol'} value={symbol} onChange={(e) => setSymbol(e.target.value)}/>

                    <select name="direction" id="direction" onChange={(e) => setDirection(e.target.value)}>
                        <option value="ABOVE">Above</option>
                        <option value="BELOW">Below</option>
                    </select>

                    <input type={'number'} placeholder={'Trigger'} value={trigger} onChange={(e) => setTrigger(e.target.value)}/>
                    <input type={'text'} placeholder={'Message'} value={message} onChange={(e) => setMessage(e.target.value)}/>

                    <input type="submit" value="Submit"/>
                </form>
            </div>


        </section>
    )
}

export default NewAlertPage;
