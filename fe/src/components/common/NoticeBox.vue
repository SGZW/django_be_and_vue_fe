<template>
    <Menu-item name="notice-box">
        <Poptip title="通知中心" placement="bottom-end">
            <Badge :count="noticeNum">
                <Icon type="ios-bell-outline" size="26"></Icon>
            </Badge>
            <div class="notice-list" slot="content">
                <ul>
                    <li v-for="notice in common.noticeBox">{{ notice.notice_time }}: {{ notice.content }}</li>
                </ul>
            </div>
        </Poptip>
    </Menu-item>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .notice-list{

    }
</style>

<script>
    import { mapState, mapGetters } from 'vuex';

    export default {
        name: 'notice-box',
        data: () => {
            return {};
        },
        computed: {
            ...mapState([
                'common',
            ]),
            ...mapGetters([
                'noticeNum',
            ]),
        },
    };
</script>
