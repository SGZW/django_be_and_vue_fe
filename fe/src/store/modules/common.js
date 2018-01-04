/*
headerBar
    logo
    menu
    notifications
    user
sidebar
*/
import * as types from '../mutation-types';
import { Notice } from 'iview';

// initial state
const state = {
    appList: [
        {
            text: 'TCS',
            link: 'https://tcs.bytedance.net/',
        },
    ],
    noticeBox: [
    ],
};

// getters
const getters = {
    noticeNum: state => {
        return state.noticeBox.length;
    },
};

// actions
const actions = {
};

// mutations
const mutations = {
    [types.RECEIVE_NOTIFY] (state, { notice }) {
        state.noticeBox.push(notice);
        Notice.info({
            title: notice.send_time,
            desc: notice.content,
            duration: 0,
            top: 50,
        });
    },
};

export default {
    state,
    getters,
    actions,
    mutations,
};
