import React, {useState, createContext, useContext, useEffect} from 'react';

const Context = createContext();
export const useC = () => useContext(Context)

function ContextProvider({ children }){

    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const [username, setUsername] = useState(null)
    const [haveApi, setHaveApi] = useState(false)
    const [loading, setLoading] = useState(false)
    const [systemMsg, setSystemMsg] = useState('')

    useEffect(() => {
        setTimeout(() => {
            setSystemMsg('')
        }, 5000)
    }, [systemMsg])

    const data = {
        isAuthenticated: [isAuthenticated, setIsAuthenticated],
        username: [username, setUsername],
        haveApi: [haveApi, setHaveApi],
        loading: [loading, setLoading],
        systemMsg: [systemMsg, setSystemMsg],
    }

    return (
        <Context.Provider value={data}>
            {children}
        </Context.Provider>
    )
}

export default ContextProvider;
