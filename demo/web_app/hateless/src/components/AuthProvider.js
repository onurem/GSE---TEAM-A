import React from 'react'
import { Navigate, useLocation } from 'react-router-dom';
import { fakeAuthProvider, fetchApi } from './Utils';

let AuthContext = React.createContext(null);

function useAuth() {
    return React.useContext(AuthContext);
}

function RequireAuth({ children }) {
    let auth = useAuth();
    let location = useLocation();

    if (!auth.user) {
        // Redirect them to the /login page, but save the current location they were
        // trying to go to when they were redirected. This allows us to send them
        // along to that page after they login, which is a nicer user experience
        // than dropping them off on the home page.
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    return children;
}

export default function AuthProvider(props) {
    let [user, setUser] = React.useState(null);

    let signin = (newUser, password, callback, errCallback) => {
        // return fakeAuthProvider.signin(() => {
        //     setUser(newUser);
        //     callback();
        // });
        let formData = new FormData();
        formData.append('email', newUser)
        formData.append('password', password)

        fetchApi('https://hateless.herokuapp.com/auth/login', {
            method: 'POST',
            body: formData
        })
            .then(rs => {
                setUser(newUser);
                callback();
            })
            .catch(err => {
                console.log("Error ", err)
                errCallback(err)
            })
    };

    let signout = callback => {
        return fakeAuthProvider.signout(() => {
            setUser(null);
            callback();
        });
    };
    let value = { user, signin, signout };

    return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>;
}

export { useAuth, RequireAuth };

