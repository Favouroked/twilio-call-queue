import axios from 'axios';

export function callQueueDetails() {
    return axios.get('http://localhost:5000/queue/details');
}