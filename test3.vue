<template>  
  <div>  
    <!-- 原始表格 -->  
    <el-table  
      :data="tableData"  
      style="width: 100%"  
      @selection-change="handleSelectionChange"  
      ref="multipleTable"  
    >  
      <el-table-column  
        type="selection"  
        width="55"  
      ></el-table-column>  
      <el-table-column prop="date" label="日期" width="180"></el-table-column>  
      <el-table-column prop="name" label="姓名" width="180"></el-table-column>  
      <el-table-column prop="address" label="地址"></el-table-column>  
    </el-table>  
  
    <!-- 按钮触发对话框 -->  
    <el-button type="primary" @click="dialogVisible = true">查看选择</el-button>  
  
    <!-- 对话框 -->  
    <el-dialog  
      title="选择详情"  
      :visible.sync="dialogVisible"  
      width="50%"  
    >  
    <!-- 选择列表 -->  
      <el-select v-model="selectedOption" placeholder="请选择">  
        <el-option  
          v-for="item in options"  
          :key="item.value"  
          :label="item.label"  
          :value="item.value"  
        ></el-option>  
        <el-option  
          value="create"  
          label="创建新选项"  
          disabled  
          style="color: blue; cursor: pointer;"  
          @click.native.stop="createNewOption"  
        ></el-option>  
      </el-select>  
      <el-button type="primary" @click="createNewDialogVisible = true">创建新选项</el-button>  
      <!-- 假设的表单部分 -->  
      <div>  
        <el-input placeholder="请输入一些内容"></el-input>  
      </div>  
  
      <!-- 选择数据的表格 -->  
      <el-table :data="selectedData" style="width: 100%" height="200px">  
        <el-table-column prop="date" label="日期" width="180"></el-table-column>  
        <el-table-column prop="name" label="姓名" width="180"></el-table-column>  
        <el-table-column prop="address" label="地址"></el-table-column>  
      </el-table>  
  
      <span slot="footer" class="dialog-footer">  
        <el-button @click="dialogVisible = false">取 消</el-button>  
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>  
      </span>  
    </el-dialog>  
    <!-- 对话框：创建新选项 -->  
    <el-dialog  
      title="创建新选项"  
      :visible.sync="createNewDialogVisible"  
      width="40%"  
    >  
      <el-form :model="newOptionForm">  
        <el-form-item label="名称">  
          <el-input v-model="newOptionForm.name" autocomplete="off"></el-input>  
        </el-form-item>  
        <!-- 可以添加更多表单项，如选择框等 -->  
  
        <span slot="footer" class="dialog-footer">  
          <el-button @click="createNewDialogVisible = false">取 消</el-button>  
          <el-button type="primary" @click="saveNewOption">保 存</el-button>  
        </span>  
      </el-form>  
    </el-dialog>  
  </div>  
</template>  
  
<script>  
export default {  
  data() {  
    return {  
      tableData: [  
        // 假设有十条数据  
        { date: '2023-01-01', name: '张三', address: '地址1' },  
        { date: '2023-01-02', name: '李四', address: '地址2' },  
        // ... 添加更多数据  
        { date: '2023-01-10', name: '王五', address: '地址10' },  
      ],  
      options: [  
        { value: 'option1', label: '选项1' },  
        { value: 'option2', label: '选项2' },  
        // ...添加更多默认选项...  
      ],  
      selectedOption: '',  
      createNewDialogVisible: false,  
      newOptionForm: {  
        name: ''  
        // ...添加其他表单字段...  
      },
      selectedData: [],  
      dialogVisible: false,  
    };  
  },  
  methods: {  
    handleSelect(index, row) {  
      this.selectedData.push(row);  
    },
    toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.selectedData.toggleRowSelection(row);
          });
        } else {
          this.$refs.selectedData.clearSelection();
        }
      },
      handleSelectionChange(val) {
        this.selectedData = val;
      },
      handleDropdownVisibility(visible) {  
      if (!visible && this.selectedOption === 'create') {  
        this.createNewDialogVisible = true;  
        this.selectedOption = ''; // 重置选择  
      }  
    },  
  
    createNewOption() {  
      // 实际上这个方法不需要内容，因为点击事件被handleDropdownVisibility拦截了  
    },  
  
    saveNewOption() {  
      // 假设保存新选项到options数组中  
      const newOption = {  
        value: `option${this.options.length + 1}`, // 简单的唯一值生成  
        label: this.newOptionForm.name  
      };  
      this.options.push(newOption);  
      this.newOptionForm.name = ''; // 清空输入框  
      this.createNewDialogVisible = false; // 关闭对话框  
    }  
  },  
};  
</script>
