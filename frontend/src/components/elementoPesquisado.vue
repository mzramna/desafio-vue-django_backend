<template>
  <tr>
    <td><img :src="produto.imagem" :alt="produto.nome" height="50" width:auto /></td>
    <td>
      <a :href="produto.link">{{ produto.nome }}</a>
    </td>
    <td>{{ produto.categoria }}</td>
    <td>{{ produto.dosagem }}</td>
    <td>{{ produto.quantidade }}</td>
    <td>{{ produto.marca }}</td>
    <td>{{ produto.preco }}</td>
    <td>{{ produto.desconto }}</td>
    <td>{{ produto.descontoPctg }}</td>
  </tr>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { Produto } from "../produto";

@Options({})
export default class ElementoPesquisado extends Vue {
  @Prop() produto!: Produto;

  // isDefined(): boolean {
  //   return this.produtos !== undefined;
  // }
  // v-if="isDefined()"
}
</script>

<!-- Add "scoped" attribute to limit CSS to tdis component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
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
