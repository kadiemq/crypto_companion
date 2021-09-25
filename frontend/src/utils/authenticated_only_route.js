import {Redirect, Route} from "react-router-dom";
import {useC} from "./context";
import React from "react";

export default function AuthenticatedOnly({ children, ...rest }) {
    const {isAuthenticated} = useC()
    const [isAuthenticatedValue] = isAuthenticated
    return (
        <Route
            {...rest}
            render={({ location }) =>
                isAuthenticatedValue ? (
                    children
                ) : (
                    <Redirect
                        to={{
                            pathname: "/login",
                            state: { from: location }
                        }}
                    />
                )
            }
        />
    )
}
