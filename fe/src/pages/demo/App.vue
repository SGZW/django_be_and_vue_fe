<template>
    <div id="app">
        <header>
            <!--headroom和iview有不兼容，先禁用-->
            <!--<headroom>-->
                <HeaderBar>

                </HeaderBar>
            <!--</headroom>-->
        </header>
        <div class="main">
            <Row type="flex">
                 <i-col :span="layout.SideBarSpan" v-if="layout.SideBarSpan > 0">
                    <SideBar>
                        <Menu accordion width="auto" :active-name="activeName">
                            <Menu-item name="1" onclick="window.location.href='#/'">
                                    <Icon type="ios-paper"></Icon>
                                      迁入管理
                            </Menu-item>
                            <Menu-item name="2" onclick="window.location.href='#/migrate/'">
                                    <Icon type="ios-paper"></Icon>
                                      迁出查询
                            </Menu-item>
                            <Menu-item name="3" onclick="window.location.href='#/id_card/'">
                                    <Icon type="ios-paper"></Icon>
                                      身份证管理
                            </Menu-item>
                        </Menu>
                    </SideBar>
                </i-col>
                <i-col :span="layout.ContainerSpan">
                    <router-view></router-view>
                </i-col>
            </Row>
        </div>
        <footer>
            <FootRoom></FootRoom>
        </footer>
    </div>
</template>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
    /*fix headroom*/
    .headroom-wrapper {
        height: auto !important;
    }
    .main{
        padding: 10px;
    }
</style>

<script>
    import { headroom } from 'vue-headroom';
    import HeaderBar from '@/containers/common/HeaderBar';
    import SideBar from '@/components/common/SideBar';
    import FootRoom from '@/components/common/FootRoom';

    import { mapState } from 'vuex';

    export default {
        name: 'app',
        components: {
            headroom,
            HeaderBar,
            SideBar,
            FootRoom,
        },
        data () {
            return {
                activeName: '1',
            };
        },
        methods: {
        },
        computed: {
            ...mapState([
                'layout',
            ]),
        },
    };
</script>
