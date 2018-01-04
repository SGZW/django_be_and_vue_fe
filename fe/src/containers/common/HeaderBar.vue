<template>
    <div class="header-bar">
        <Menu mode="horizontal">
            <Row type="flex" align="middle">
                <i-col span="4">
                    <div class="header-bar-logo">
                        <Logo></Logo>
                    </div>
                </i-col>
                <i-col span="9">

                </i-col>
                <i-col span="6" offset="5">
                    <div class="header-bar-right">
                        <AppPad></AppPad>
                        <NoticeBox></NoticeBox>
                        <UserBox></UserBox>
                    </div>
                </i-col>
            </Row>
        </Menu>
        <div class="clear-fix"></div>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .header-bar{
    }
    .header-bar-logo{
        float: left;
    }
    .header-bar-left{
    }
    .header-bar-right{
        float: right;
    }
    .clear-fix{
        clear: both;
    }
</style>

<script>
    import { mapState } from 'vuex';
    import Logo from '@/components/common/Logo';
    import AppPad from '@/components/common/AppPad';
    import NoticeBox from '@/components/common/NoticeBox';
    import UserBox from '@/components/common/UserBox';

    export default {
        name: 'header-bar',
        data: () => {
            return {
                balance: '',
                costs: '',
                activeNum: '',
                totalNum: '',
            };
        },
        components: {
            Logo,
            AppPad,
            NoticeBox,
            UserBox,
        },
        computed: mapState([
            'topNav',
            'appPad',
            'NBox',
            'logo',
            'user',
        ]),
    };
</script>
