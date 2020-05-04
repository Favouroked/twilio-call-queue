import React from 'react';
import './App.css';

import {callQueueDetails} from './utils/api';

class App extends React.Component {

    state = {
        count: 0
    };

    componentDidMount() {
        callQueueDetails()
            .then(res => {
                const count = res.data.current_size;
                this.setState({count})
            })
            .catch(e => {
                console.error(e.response);
                alert('An error occurred');
            })
    }

    render() {
        const {count} = this.state;
        return <div className={'home'}>
            <h3 className={'home-title'}>Customer Support Call Center</h3>
            <p className={'home-description'}>There are {count} callers in the queue.</p>

            {count !== 0 && <a href={'tel:+12183962975'} className={'home-button'}>Attend to Caller</a>}
        </div>;
    }

}

export default App;
