<template>
    <div class="logo">
        <span>
            <i-button type="text" @click="ShiftSidebar">
                <Icon type="navicon" size="24"></Icon>
            </i-button>
            {{ layout.logo.text }}
        </span>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .logo {
        /*width: 180px;*/
        font-size: 18px;
        font-weight: 900;
        color: #3399ff;
        margin: 0 auto;
    }
</style>

<script>
    import { mapActions, mapState } from 'vuex';

    export default {
        name: 'logo',
        data: () => {
            return {};
        },
        methods: mapActions([
            'ShiftSidebar',
        ]),
        computed: mapState([
            'layout',
        ]),
    };
</script>
