import { shallowMount } from "@vue/test-utils";
import ElementoPesquisa from "@/components/elementoPesquisa.vue";

describe("elementoPesquisa.vue", () => {
  it("renders props.msg when passed", () => {
    const produto = "new message";
    const wrapper = shallowMount(ElementoPesquisa, {
      props: { produto },
    });
    expect(wrapper.text()).toMatch(produto);
  });
});
