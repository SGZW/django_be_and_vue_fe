<template>
    <Card>
        <p slot="title">
             身份证管理
        </p>
        <Form inline>

            <FormItem label="身份证号">
                <Input v-model="search_form.id" type="text" placeholder="请填入身份证号"></Input>
            </FormItem>
            <FormItem label="性别">
                <Select v-model="search_form.sex" placeholder="请选择性别" style="width: 150px;">
                    <Option v-for="i in sex_type" :value="i.value" :key="i.value">{{ i.label }}</Option>
                </Select>
            </FormItem>
            <FormItem label="民族">
                <Input v-model="search_form.nation" type="text" placeholder="请选择民族"></Input>
            </FormItem>
            <FormItem label="姓名">
                <Input v-model="search_form.name" type="text" placeholder="请选择姓名"></Input>
            </FormItem>
        </Form>
        <Form inline>
            <FormItem>
                <Button type="primary" @click="search">查询</Button>
            </FormItem>
            <FormItem>
                <Button type="primary" @click="add">添加</Button>
            </FormItem>
        </Form>
        <Table stripe border :columns="data_table.column" :data="data_table.data"></Table>
        <Modal v-model="add_form.seen" :title="add_form.title" width="800" :styles="{top: '40px'}" @on-ok="save" okText="新增">
                <Form>
                    <FormItem label="身份证" >
                        <Input v-model="add_form.id" type="text"></Input>
                    </FormItem>
                    <FormItem label="性别">
                        <Select v-model="add_form.sex" placeholder="请选择性别" style="width: 150px;">
                            <Option v-for="i in sex_type" :value="i.value" :key="i.value">{{ i.label }}</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="民族" >
                        <Input v-model="add_form.nation" type="text"></Input>
                    </FormItem>
                    <FormItem label="姓名" >
                        <Input v-model="add_form.name"  type="text"></Input>
                    </FormItem>
                    <FormItem label="地址">
                        <Input v-model="add_form.address"  type="text"></Input>
                    </FormItem>
                    <FormItem label="出生日期" >
                        <DatePicker type="date"  placeholder="请选择日期" style="width: 200px" @on-change="handleChange"></DatePicker>
                    </FormItem>
                </Form>
        </Modal>
    </Card>
</template>

<script>
    import request from '@/libs/request';
    export default {
        data () {
            return {
                name: 'idcard',
                add_form: {
                    seen: false,
                    title: '身份证添加',
                    id: '',
                    sex: '',
                    nation: '',
                    name: '',
                    address: '',
                    born: '',
                },
                search_form: {
                    id: '',
                    sex: '',
                    nation: '',
                    name: '',
                },
                sex_type: [
                    {
                        label: '男',
                        value: '男',
                    },
                    {
                        label: '女',
                        value: '女',
                    },
                ],
                data_table: {
                    column: [
                        {
                            title: '身份证号',
                            key: 'id',
                            width: 180,
                            ellipsis: true,
                        },
                        {
                            title: '姓名',
                            key: 'name',
                        },
                        {
                            title: '性别',
                            key: 'sex',
                        },
                        {
                            title: '民族',
                            key: 'nation',
                        },
                        {
                            title: '地址',
                            key: 'address',
                        },
                        {
                            title: '出生日期',
                            key: 'born',
                        },
                    ],
                    data: [],
                },
            };
        },
        methods: {
            search () {
                request({
                    url: '/api/get_card_search_data/',
                    method: 'get',
                    params: {
                        id: this.search_form.id,
                        sex: this.search_form.sex,
                        nation: this.search_form.nation,
                        name: this.search_form.name,
                    },
                }).then((res) => {
                    this.data_table.data = res.search_data;
                });
            },
            refresh () {
                request({
                    url: '/api/get_card_init_data/',
                    method: 'get',
                }).then((res) => {
                    this.data_table.data = res.init_data;
                });
            },
            add () {
                this.add_form.seen = true;
            },
            save () {
                if (this.add_form.id.trim() === '') {
                    this.$Message.info('身份证号为空');
                    return;
                }
                if (this.add_form.sex.trim() === '') {
                    this.$Message.info('性别为空');
                    return;
                }
                if (this.add_form.name.trim() === '') {
                    this.$Message.info('姓名为空');
                    return;
                }
                if (this.add_form.nation.trim() === '') {
                    this.$Message.info('民族为空');
                    return;
                }
                if (this.add_form.id.trim() === '') {
                    this.$Message.info('地址为空');
                    return;
                }
                if (this.add_form.born.trim() === '') {
                    this.$Message.info('出生日期为空');
                    return;
                }
                request({
                    url: '/api/add_card_data/',
                    method: 'get',
                    params: {
                        id: this.add_form.id.trim(),
                        sex: this.add_form.sex.trim(),
                        name: this.add_form.name.trim(),
                        nation: this.add_form.nation.trim(),
                        address: this.add_form.address.trim(),
                        born: this.add_form.born.trim(),
                    },
                }).then((res) => {
                    this.$Message.info(res.status);
                    this.refresh();
                });
            },
            handleChange (date) {
                this.add_form.born = date;
            },
        },
        mounted () {
            this.refresh();
        },
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
