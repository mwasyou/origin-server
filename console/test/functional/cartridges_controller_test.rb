require File.expand_path('../../test_helper', __FILE__)

class CartridgesControllerTest < ActionController::TestCase

  def with_testable_app(remove_carts=false)
    use_app(:cart_testable_app) { Application.new({:name => "scaled", :cartridge => 'ruby-1.9', :as => new_named_user('user_with_cartridge_testable_app')}) }.tap do |app|
      if remove_carts
        app.cartridges.each do |cart|
          cart.destroy unless cart.name == app.framework
        end
      end
    end
  end

  test "should create one cartridge" do
    with_testable_app(true)

    post(:create, get_post_form)
    assert cart = assigns(:cartridge)
    assert cart.errors.empty?, cart.errors.inspect
    assert_response :success
    assert_template :next_steps
  end

  test "should create two cartridges" do
    with_testable_app(true)

    post(:create, get_post_form)
    assert cart = assigns(:cartridge)
    assert cart.errors.empty?, cart.errors.inspect
    assert_response :success
    assert_template :next_steps

    post_form = get_post_form
    post_form[:cartridge][:name] = 'cron-1.4'
    post(:create, post_form)
    assert cart = assigns(:cartridge)
    assert cart.errors.empty?, cart.errors.inspect

    assert_response :success
    assert_template :next_steps
  end

  test "should error out if cartridge is installed" do
    with_testable_app(true)

    post(:create, get_post_form)
    assert cart = assigns(:cartridge)
    assert cart.errors.empty?, cart.errors.inspect
    assert_response :success
    assert_template :next_steps

    post(:create, get_post_form)
    assert_response :success
    assert cart = assigns(:cartridge)
    assert !cart.errors.empty?, cart.errors.inspect
    assert cart.errors[:base].present?
    assert_equal 1, cart.errors[:base].length

    assert_response :success
    assert_template 'cartridge_types/show'
  end

  #test "should be able to view next steps cartridge page" do
  #  with_testable_app(true)

  #  get :next_steps, get_post_form
  #  assert_response :success
  #  assert_template :next_steps
  #end

  def get_post_form
    {:cartridge => {:name => 'mysql-5.1', :type => 'embedded'},
     :application_id => with_testable_app.id,
     :domain_id => @domain.id}
  end
end
