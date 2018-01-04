<template>
    <div class="side-bar">
        <slot>
            I'm SideBar.
        </slot>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .side-bar {
    }
</style>

<script>
    export default {
        name: 'side-bar',
        data: () => {
            return {};
        },
    };
</script>
