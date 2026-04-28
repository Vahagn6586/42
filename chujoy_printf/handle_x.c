/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_x.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 18:15:29 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/11 18:15:31 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_x(va_list *arg)
{
	unsigned int	val;
	char			*ret;
	int				ret_val;

	val = va_arg(*arg, unsigned int);
	ret = ft_itoa_base_low(val, 16);
	ret_val = ft_strlen(ret);
	ft_putstr(ret);
	free(ret);
	return (ret_val);
}
