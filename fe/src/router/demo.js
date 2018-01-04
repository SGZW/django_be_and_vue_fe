import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/pages/Index';
import Migrate from '@/pages/migrate';
import IDcard from '@/pages/demo/idcard';
Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'index',
            component: Index,
        },
        {
            path: '/migrate/',
            name: 'migrate',
            component: Migrate,
        },
        {
            path: '/id_card/',
            name: 'idcard',
            component: IDcard,
        },
    ],
});
