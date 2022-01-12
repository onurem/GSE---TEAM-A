const fakeAuthProvider = {
    isAuthenticated: false,
    signin(callback) {
        fakeAuthProvider.isAuthenticated = true;
        setTimeout(callback, 100); // fake async
    },
    signout(callback) {
        fakeAuthProvider.isAuthenticated = false;
        setTimeout(callback, 100);
    }
};

export const fetchApi = (url, opts) => fetch(url, opts)
    .then(res => {
        if (res.ok) return res.json();
        throw res;
    })
    .then(rs => rs)
    .catch(error =>
        error.json()
            .then(err_msg => Promise.reject(`[${error.status}:${err_msg['status']}] ${err_msg['message']}`)))

export { fakeAuthProvider };