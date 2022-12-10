import React from 'react'


export default class connectionExample extends React.Component {
    componentDidMount() {
        const url = 'http://127.0.0.1:8000/api/threads/'
        fetch(url).then((response) => response.json()).then((data) => console.log(data));
    }
    render() {
        return <div>Connected!</div>
    }
}
// export function MainPage() {
//     return (
//         <>Main</>
//     )
// }