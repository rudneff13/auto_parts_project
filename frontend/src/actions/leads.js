import axios from 'axios';

import { GET_LEADS, DELETE_LEAD } from "./types";

// GET LEADS
export const getLeads = () => dispatch => {
    axios.get('/api/products/')
        .then(res => {
            dispatch({
                type: GET_LEADS,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

// DELETE LEAD
export const deleteLead = (pk) => dispatch => {
    axios.delete(`/api/products/${pk}/`)
        .then(res => {
            dispatch({
                type: DELETE_LEAD,
                payload: pk
            });
        }).catch(err => console.log(err));
};
