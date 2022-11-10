<template>
  <form @submit.prevent="onSubmit">
    <input
      v-model="produtoPesquisado"
      placeholder="produtoPesquisado"
      type="text"
      aria-label="produtoPesquisado"
    />
    <input
      v-model="quantidadeProdutos"
      placeholder="24"
      type="number"
      aria-label="quantidadeProdutos"
    />
    <button type="submit" aria-label="Submit">Submit</button>
  </form>
  <div v-if="emPesquisa">pesquisando....</div>
  <table v-if="exibir" class="striped">
    <thead>
      <tr>
        <th>imagem</th>
        <th>nome</th>
        <th>categoria</th>
        <th>dosagem</th>
        <th>quantidade</th>
        <th>link</th>
        <th>marca</th>
        <th>preco</th>
        <th>desconto</th>
        <th>descontoPctg</th>
      </tr>
    </thead>
    <tbody>
      <elementoPesquisado v-for="produto in produtos" :key="produto.nome" :produto="produto" />
    </tbody>
  </table>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import ElementoPesquisado from "./components/elementoPesquisado.vue";
import { Produto } from "./produto";

@Options({
  components: {
    elementoPesquisado: ElementoPesquisado,
  },
})
export default class App extends Vue {
  exibir = false;

  emPesquisa = false;

  produtos: Produto[] = [];

  produtoPesquisado = "";

  quantidadeProdutos = 24;

  onSubmit(): void {
    this.exibir = false;
    this.emPesquisa = true;
    setTimeout(() => {
      this.produtos = this.pesquisar(this.produtoPesquisado, this.quantidadeProdutos);
      this.emPesquisa = false;
      this.exibir = true;
      console.log(this.produtos);
    }, 500);
  }

  pesquisar(produtoPesquisado: string, quantidadeProdutos: number): Produto[] {
    console.log(produtoPesquisado, quantidadeProdutos);
    console.log(this.exibir);
    return [
      {
        imagem: "teste",
        nome: "teste",
        categoria: "teste",
        dosagem: 0,
        quantidade: 0,
        link: "teste",
        marca: "teste",
        preco: 0,
        desconto: 0,
        descontoPctg: 0,
      },
      {
        imagem: "teste",
        nome: "teste",
        categoria: "teste",
        dosagem: 0,
        quantidade: 0,
        link: "teste",
        marca: "teste",
        preco: 0,
        desconto: 0,
        descontoPctg: 0,
      },
      {
        imagem: "teste",
        nome: "teste",
        categoria: "teste",
        dosagem: 0,
        quantidade: 0,
        link: "teste",
        marca: "teste",
        preco: 0,
        desconto: 0,
        descontoPctg: 0,
      },
    ];
  }
  // onSubmit(): void {
  //   this.exibir = false;
  //   this.emPesquisa = true;
  //   this.produtos = this.pesquisar(this.produtoPesquisado, this.quantidadeProdutos);
  //   this.emPesquisa = false;
  //   this.exibir = true;
  //   console.log(this.produtos);
  // }

  // async pesquisar(produtoPesquisado: string, quantidadeProdutos: number): Promise<Produto[]> {
  //   let retorno = [] as Produto[];
  //   const tmp = setTimeout(async () => {
  //     console.log(produtoPesquisado, quantidadeProdutos);
  //     console.log(this.exibir);
  //     retorno = [
  //       {
  //         imagem: "teste",
  //         nome: "teste",
  //         categoria: "teste",
  //         dosagem: 0,
  //         quantidade: 0,
  //         link: "teste",
  //         marca: "teste",
  //         preco: 0,
  //         desconto: 0,
  //         descontoPctg: 0,
  //       },
  //       {
  //         imagem: "teste",
  //         nome: "teste",
  //         categoria: "teste",
  //         dosagem: 0,
  //         quantidade: 0,
  //         link: "teste",
  //         marca: "teste",
  //         preco: 0,
  //         desconto: 0,
  //         descontoPctg: 0,
  //       },
  //       {
  //         imagem: "teste",
  //         nome: "teste",
  //         categoria: "teste",
  //         dosagem: 0,
  //         quantidade: 0,
  //         link: "teste",
  //         marca: "teste",
  //         preco: 0,
  //         desconto: 0,
  //         descontoPctg: 0,
  //       },
  //     ];
  //   }, 500);
  //   console.log(tmp);
  //   return retorno;
  // }
}
</script>

<style lang="scss">
@charset "UTF-8";

@import "~materialize-css/sass/components/mixins";

// all colors:
// @import "~materialize-css/sass/components/color";

// BEGIN: only specific colors
@import "~vue-materialize/sass/color";
// include colors you need
@include do("include-color", "black", "base");
@include do("include-color", "white", "base");
@import "~vue-materialize/sass/colorProcessor";
// END: only specific colors

@import "~materialize-css/sass/components/variables";
@import "~materialize-css/sass/components/normalize";
@import "~materialize-css/sass/components/typography";
@import "~materialize-css/sass/components/global";

// modify variables here
// all available sass variables:
// https://github.com/Dogfalo/materialize/blob/master/sass/components/_variables.scss
// e.g. $dropdown-bg-color: black;

// css only, no JS needed for these
// activate only what you need
$roboto-font-path: "~materialize-css/fonts/roboto/";
@import "~materialize-css/sass/components/roboto";
@import "~materialize-css/sass/components/icons-material-design";
 // icons are no long included in materializeCSS
@import "~materialize-css/sass/components/buttons";
@import "~materialize-css/sass/components/grid";
@import "~materialize-css/sass/components/navbar";
@import "~materialize-css/sass/components/preloader";
@import "~vue-materialize/sass/forms";

// css for js modules
// activate only what you need
@import "~materialize-css/sass/components/cards";
@import "~materialize-css/sass/components/sideNav";
@import "~materialize-css/sass/components/dropdown";
@import "~materialize-css/sass/components/modal";
@import "~materialize-css/sass/components/collapsible";
@import "~materialize-css/sass/components/table_of_contents"; // scrollspy
@import "~materialize-css/sass/components/forms/input-fields";
// ----- no js but need to be after input-fields
@import "~materialize-css/sass/components/forms/checkboxes";
@import "~materialize-css/sass/components/forms/radio-buttons";
// -----
@import "~materialize-css/sass/components/forms/switches";
@import "~materialize-css/sass/components/forms/select";
// need to be after input-fields
@import "~materialize-css/sass/components/toast";
@import "~materialize-css/sass/components/tooltip";

// NOT implemented yet:
// @import "~materialize-css/sass/components/tabs";
// @import "~materialize-css/sass/components/slider";
// @import "~materialize-css/sass/components/date_picker/default";
// @import "~materialize-css/sass/components/date_picker/default.date";
// @import "~materialize-css/sass/components/date_picker/default.time";
// @import "~materialize-css/sass/components/forms/file-input";
// @import "~materialize-css/sass/components/forms/range";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
