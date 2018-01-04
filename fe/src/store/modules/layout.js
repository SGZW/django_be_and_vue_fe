/*
headerBar
    logo
    menu
    notifications
    user
sidebar
*/
import * as types from '../mutation-types';
import Const from '../../libs/const';

// initial state
const state = {
    SideBarSpan: Const.defaultSideBarSpan,
    ContainerSpan: Const.defaultContaninerSpan,
    logo: {
        text: '派出所户籍管理系统',
    },
};

// getters
const getters = {
};

// actions
const actions = {
    ShiftSidebar ({ commit }) {
        commit(types.SHIFT_SIDEBAR);
    },
};

// mutations
const mutations = {
    [types.SHIFT_SIDEBAR] (state) {
        if (state.SideBarSpan === Const.defaultSideBarSpan) {
            state.SideBarSpan = 0;
            state.ContainerSpan = 24;
        } else {
            state.SideBarSpan = Const.defaultSideBarSpan;
            state.ContainerSpan = Const.defaultContaninerSpan;
        }
    },
};

export default {
    state,
    getters,
    actions,
    mutations,
};
